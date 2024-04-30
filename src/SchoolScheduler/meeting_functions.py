from base import *
from read_files import *
import time




# create an empty table with groups representing the rows and periods representing the columns
def create_table():

    # initialise timetable & create rows
    data = {('main', 'group'): Groups}
    df = pd.DataFrame(data)

    # create columns (mon - fri, period 1 - period 5)
    for day in Days:

        for i in range(1,6):
            
            # assign 0 to each cell, representing an empty cell
            df[(day, f'p{i}')] = np.zeros(len(Groups))


    return df
    



# creates the meetings which will later be assigned to each timetable slot
def create_meetings():

    Meetings = {}

    # iterate through all subjects
    for sub in Subjects:

        # create a list with all teachers which specialty matches the subject
        Meetings[sub.name] = []
        teachers_with_matching_subject = [teacher for teacher in Teachers if sub.name in teacher.subjects]

        # create meetings with n number of teachers and n number of classes and add it to a lsit of meetings
        for i in range(int(len(teachers_with_matching_subject) / classes_per_group)):

            Meetings[sub.name].append(Meeting(f'{sub.name}{i+1}', teachers_with_matching_subject[i*classes_per_group : classes_per_group + i*classes_per_group]))


    return Meetings



# returns a dataframe which contains the number of lessons required per subject per group
def subject_tracker(df):

    strack = pd.DataFrame()
    strack.index = df.index.tolist()

    for sub in Subjects:

        strack[sub.name] = sub.hours


    return strack




def assign_meetings(df):

    rows = df.index.tolist()
    columns = df.columns.tolist()
    columns.pop(0)
    strack = subject_tracker(df)

    # iterate through all columns one by one
    for column in columns:

        # iterate through all rows one by one
        for row in rows:

            z = 0

            # loops a maximum of 100 times
            while z < 100:

                z+=1
                isbreak = False

                # choose a random subject and randomize the order of meetings of that subject
                random_subject = random.choices(Subjects, weights=strack.loc[row].tolist())[0]
                random.shuffle(Meetings[random_subject.name])


                for meeting in Meetings[random_subject.name]:

                    # checks that the selected meeting is not already in the same column
                    if meeting not in df[column].tolist():

                        # insert the meeting into the cell 
                        df.loc[row, column] = meeting
                        strack.loc[row, random_subject.name] -= 1    # remove 1 from the cell corresponding to the subject and group
                        isbreak = True
                        break
                
                if isbreak == True:

                    break
            

    return df, strack



# fill any remaining meetings that assign_meetings missed
def fill_unfilled_meetings(df, missing_subjects):

    missing_subjects_copy = missing_subjects.copy()
    rows = df.index.tolist()
    cols = df.columns.tolist()

    # iterate through all rows one by one
    for row in rows:

        # get the indices of all periods in the row which are unassigned
        unfilled_periods = np.where(df.loc[row].values == 0)[0]

        # iterate through the indices of each missing period
        for col_index in unfilled_periods:

            missing_subjects_list = []
            isbreak = False
            
            # makes a list of all the lessons that the group is missing
            for i, val in enumerate(missing_subjects.loc[row]):

                for j in range(val):

                    missing_subjects_list.append(missing_subjects.columns[i])
                

            # iterate through all columns one by one
            for col in cols:
                
                # skip over the column containing the student objects
                if col == ('main', 'group'):
                    continue
                
                # iterate through each missing lesson
                for sub in missing_subjects_list:
                    
                    # iterate through each meeting corresponding to the missing subject of the lesson
                    for meeting in Meetings[sub]:

                        # moves the current cell to the unassigned period and inserts the missing lesson into the current cell
                        if meeting not in df[col].tolist():

                            if df.loc[row, col] not in df.iloc[:, col_index].tolist():

                                df.iloc[df.index.get_loc(row), col_index] = df.loc[row,col]
                                df.loc[row, col] = meeting
                                missing_subjects.loc[row, sub] -= 1
                                isbreak = True

                        if isbreak == True:
                            break

                    if isbreak == True:
                        break

                if isbreak == True:
                    break


    return df, missing_subjects, not missing_subjects.equals(missing_subjects_copy)



# evaluates the total error of the timetable
def objective_function(timetable):

    hc_breached = 9999
    skip = False
    strack = subject_tracker(timetable)
    subject_timetable = readable_timetable(timetable, True)
    rows = timetable.index.tolist()
    cols = timetable.columns.tolist()
    cols.pop(0)
    cost = pd.DataFrame(index=rows,columns=Days)
    cost = cost.fillna(0)
    
    # iterate through all columns
    for i, column in enumerate(cols):

        # iterate through all rows
        for row in rows:

            # get the meeting in the current cell
            meeting = timetable.loc[row, column]

            # checks for empty meetings
            if meeting != 0:

                # keep track of the number of lessons per subject per row
                subject = meeting.subject[:-1]
                strack.loc[row, subject] -= 1

            else:

                # report the breach of a hard constraint (students must attend exactly one meeting per period)
                cost += hc_breached
                continue

            if timetable[column].tolist().count(meeting) > 1: # checks no meetings are scheduled at the same time
                cost += hc_breached

            # checks if the current cell is the fifth period of the day
            if (i+1) % 5 == 0:

                # checks if the current cell is a core subject (soft constraint - as few core subjects as possible to be assigned to the final period of any given day)
                if subject in core_subjects:

                    # adds one error unit to the cell corresponding to the current day and group
                    cost.loc[row, column[0]] += 1

            # checks if any given group attends more than one lesson of any given subject per day (soft constraint - students should attend no more than one lesson of any given subject each day)
            if skip == False:

                # split list of lessons in the current row into five lists representing each day
                group_subjects = subject_timetable.loc[row].tolist()
                group_subjects = split_list(group_subjects, 5)

                for j, day in enumerate(group_subjects):

                    # adds error to the cell corresponding to the current day and group
                    cost.loc[row, cols[j*5][0]] += len(day) - len(set(day)) # number of lessons of a given subject in a day minus one

        # ensures the code above runs only once for each row
        skip = True

    # checks all groups have the correct number of lessons per subject
    if not strack.eq(0).all().all():

        # report the breach of a hard constraint (lessons for each subject must be assigned the correct number of times)
        cost += hc_breached


    # return a dataframe of days and groups with cells containing the error of each day, and the total error
    return cost.sum().sum(), cost



# this function swaps the position of two subjects on each row
def generate_neighbouring_solution(timetable, cost):

    rows = timetable.index.tolist()
    columns = timetable.columns.tolist()
    columns.pop(0)

    # iterate through each row
    for row in rows:

        # get all meetings on current row and split it into lists representing days
        group_meetings = timetable.loc[row, timetable.columns[1:]].tolist()
        group_meetings = split_list(group_meetings, 5)

        # get a list of the error of each day in the current row
        weights = cost.loc[row].tolist()

        # checks if no changes are needed
        if sum(weights) == 0:

            continue

        # create a copy of Days
        days = list(Days)
        # select a random day based on the weights
        random_day = random.choices(days, weights)[0]
        day_index = days.index(random_day)
        # remove the selected weight and day from the lists
        weights.pop(day_index)
        days.remove(random_day)

        # small chance of selecting a day with no error
        weights = [x + 0.1 for x in weights]
        # selects another random day based on the weights
        random_day2 = random.choices(days, weights)[0]
        
        # choose a random meeting from each of the selected days
        random_day_meetings = group_meetings[Days.index(random_day)]
        random_day_meetings2 = group_meetings[Days.index(random_day2)]
        random_period = random.randint(0, len(random_day_meetings) -1)
        random_period2 = random.randint(0, len(random_day_meetings2) -1)

        # checks no hard constraints are breached
        for meeting2 in Meetings[random_day_meetings2[random_period2].subject[:-1]]:

            if meeting2 not in timetable[(random_day, f'p{random_period + 1}')].tolist():

                for meeting in Meetings[random_day_meetings[random_period].subject[:-1]]:

                    if meeting not in timetable[(random_day2, f'p{random_period2 + 1}')].tolist():
                        # swaps the selected meetings around
                        timetable.loc[row, (random_day, f'p{random_period + 1}')] = meeting2
                        timetable.loc[row, (random_day2, f'p{random_period2 + 1}')] = meeting


    # return the modified timetable as a dataframe
    return timetable




def local_search(initial_solution, num_iterations):


    best_solution = initial_solution

    # generate a neighbouring solution n times
    for i in range(num_iterations):

        # create a copy of the current best solution
        best_solution_copy = best_solution.copy()

        # check the error of the current best solution
        best_value, value_table = objective_function(best_solution)

        # generate a neighbouring solution of the current best solution using the best solutions' cost dataframe
        new_solution = generate_neighbouring_solution(best_solution_copy, value_table)

        # check the error of the new solution
        new_value = objective_function(new_solution)[0]

        # checks if the new solution is more optimised than the current best solution. if so, make it the new best solution
        if new_value <= best_value:

            best_solution = new_solution.copy()


    # return the best timetable
    return best_solution



# used for splitting lists into chunks
def split_list(lst, chunk_size):

    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]



# outputs a readable version of a timetable which has either the name of the meeting or the name of the subject in each cell
def readable_timetable(table, subject_only=False):

    readable_df = pd.DataFrame()
    readable_df.index = table.index.tolist()
    cols = table.columns.tolist()
    cols.pop(0)

    # iterate through each column
    for x, col_name in enumerate(cols):
        
        ls = []

        for i in table[col_name]:

            if i == 0:

                ls.append(0)

            elif subject_only == True:

                ls.append(i.subject[:-1])

            else:

                ls.append(i.subject)
        
        readable_df[x+1] = ls


    return readable_df



# swaps the column with the least amount of core subjects with period 5 for each day
# this function is only useful if the local search is ran a small number of times
def p5_swap(timetable):

    rows = timetable.index.tolist()
    cols = timetable.columns.tolist()
    cols.pop(0)

    # used to keep track of how many core subjects are in each column
    weights = [0,0,0,0,0]

    # iterate through each column
    for i, col in enumerate(cols):

        # iterate through each row
        for row in rows:

            # checks if the current cell contains a core subject
            if timetable.loc[row, col].subject[:-1] in core_subjects:
                weights[i%5] += 1
        
        # checks if the current cell is period 5
        if i%5 == 4:

            # checks that period 5 doesn't contain the least amount of core subjects already
            if weights.index(min(weights)) != 4:

                # swap the column with the least amount of core subjects in the current day with the current days' period 5
                min_index = weights.index(min(weights))
                col_5 = timetable[col]
                timetable[col] = timetable.iloc[:, min_index + i+1 - 4]
                timetable.iloc[:, min_index + i+1 - 4] = col_5
            
            # reset the weights ready for the next loop
            weights = [0,0,0,0,0]


    # returns the modified timetable as a dataframe
    return timetable

            

# uses the school timetable to create timetables for each student and format the cells ready for the excel file
def individual_timetable(timetable, student):

    i_timetable = pd.DataFrame()
    i_timetable.index = ['p1','p2','p3','p4','p5']
    meets = []
    cols = timetable.columns.tolist()
    cols.pop(0)

    # iterate through each column
    for i, col in enumerate(cols):

        # gets the lesson of the student in the current column
        meet = timetable.loc[student.group, col]
        sub = meet.subject[:-1]

        # checks if the current subject of the lesson has sets or not
        if sub in student.sets:

            # if yes, put the student into their set
            sub2 = sub

        else:
            
            # if not, set the student to be put with their tutor group
            sub2 = 'tut'

        # gets the teacher, subject name and classroom and adds it to a list
        meets.append(f'{sub}\n\n{meet.teachers[student.sets[sub2] - 1].name}\n\n{meet.teachers[student.sets[sub2] - 1].classroom}')

        # checks if the current column is period 5
        if len(meets) == 5:

            # adds the formatted meetings to the students' individual timetable
            i_timetable[col[0]] = meets
            # reset the list ready for the next cycle
            meets = []


    # return the students' individual timetable as a dataframe
    return i_timetable




def teacher_timetable(timetable, teacher):

    t_timetable = pd.DataFrame()
    t_timetable.index = ['p1','p2','p3','p4','p5']
    meets = []
    rows = timetable.index.tolist()
    cols = timetable.columns.tolist()
    cols.pop(0)

    # iterate through each column
    for col in cols:

        no_meeting = True

        # iterate through each row
        for row in rows:

            # check if current cell is taught by the teacher
            if teacher in timetable.loc[row, col].teachers:

                # if yes, gets the subject, room, group and set and adds it to a list
                meets.append(f'{teacher.subjects[0]}\n\n{teacher.classroom}\n\n{row}{timetable.loc[row, col].teachers.index(teacher) + 1}')
                no_meeting = False
                break
        
        # check if the teacher doesn't have a meeting this period
        if no_meeting == True:

            meets.append(f'\n\nempty\n\n')

        # check if the current column is period 5
        if len(meets) == 5:

            # add the formatted meetings to the teachers' individual timetable
            t_timetable[col[0]] = meets
            meets = []


    # return the teachers' individual timetable as a dataframe
    return t_timetable

        




# this function creates the starting timetable, runs it through the local search and returns the school timetable
def process():
    
    best_solution_cost = 99999999

    # create n timetables, select the best one (timetable with the least error)
    for i in range(epochs):

        # create an empty school timetable
        df = create_table()
        # assign meetings to each cell
        df, missing_subjects = assign_meetings(df)
        
        # fills any remaining cells which still need to be filled with a meeting
        # keeps looping until fill_unfilled_meetings() can't make any more changes
        run_again = True
        while run_again:

            df, missing_subjects, run_again  = fill_unfilled_meetings(df, missing_subjects)
        
        # checks the error of the newly created timetable
        current_cost = objective_function(df)[0]

        # checks if the new timetable is better than the previous timetable
        if current_cost < best_solution_cost:

            # if so, make the new timetable the new best timetable
            best_solution_cost = current_cost
            best_solution = df
     
    df = best_solution

    # the try will fail if a timetable was not successfully created
    # this happens in very rare cases or if there are not enough teachers available to teach the number oclasses
    try:

        # run the local search n*n times
        df = local_search(df, epochs * epochs)

        df = p5_swap(df)

        # print the final school timetable and its cost to the console
        print(readable_timetable(df))
        print(f'end cost: {objective_function(df)[0]}')

    except:

        # retry the function if a timetable was not successfully created
        input('Feasible timetable failed to be created. Press ENTER to retry...')
        df = process(epochs)


    return df



 # create all meetings and add them to a global list
Meetings = create_meetings()