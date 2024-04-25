from Base import *
from Read_Files import *



def create_table():
    data = {
        ('main', 'group'): Groups
    }

    df = pd.DataFrame(data)

    for day in Days:
        for i in range(1,6):

            df[(day, f'p{i}')] = np.zeros(len(Groups))    # assign_meetings()

    return df
    


def createmeetings():

    Meetings = {}

    for sub in Subjects:

        Meetings[sub.name] = []

        teachers_with_matching_subject = [teacher for teacher in Teachers if sub.name in teacher.subjects]
        for i in range(int(len(teachers_with_matching_subject) / classes_per_group)):

            Meetings[sub.name].append(Meeting(f'{sub.name}{i+1}', [teacher.classroom for teacher in teachers_with_matching_subject], teachers_with_matching_subject[i*classes_per_group : classes_per_group + i*classes_per_group]))

    return Meetings

def subject_tracker():
    strack = pd.DataFrame()
    strack.index = df.index.tolist()
    for sub in Subjects:
        strack[sub.name] = sub.hours
    return strack

def assign_meetings():    # needs to return an array of meetings

    rows = df.index.tolist()
    columns = df.columns.tolist()
    columns.pop(0)


    # creates the amount of hours per subject per week needed
    strack = subject_tracker()

    for column in columns:

        for row in rows:

            z = 0

            while z < 100:
                z+=1
                isbreak = False
                random_subject = random.choices(Subjects, weights=strack.loc[row].tolist())[0]

                random.shuffle(Meetings[random_subject.name])

                for meeting in Meetings[random_subject.name]:
                    if meeting not in df[column].tolist():
                        df.loc[row, column] = meeting
                        strack.loc[row, random_subject.name] -= 1
                        isbreak = True
                        break
                
                if isbreak == True:
                    break
            
            

    return df, strack



def fill_unfilled_meetings():
    missing_subjects_copy = missing_subjects.copy()
    #print(missing_subjects_copy)
    rows = df.index.tolist()
    cols = df.columns.tolist()
    #cols.pop(0)
    for row in rows:



        unfilled_periods = np.where(df.loc[row].values == 0)[0]
        # for i in range(len(unfilled_periods)):
            
        #     unfilled_periods[i] +=1

        for col_index in unfilled_periods:

            missing_subjects_list = []
            isbreak = False
            
            # makes a list of the missing subjects
            for i, val in enumerate(missing_subjects.loc[row]):
                for j in range(val):
                    missing_subjects_list.append(missing_subjects.columns[i])
                


            for col in cols:
                
                if col == ('main', 'group'):
                    continue

                for sub in missing_subjects_list:

                    for meeting in Meetings[sub]:

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

def objective_function(timetable):

    hc_breached = 9999
    skip = False

    strack = subject_tracker()
    subject_timetable = readable_timetable(timetable, True)
    rows = timetable.index.tolist()
    cols = timetable.columns.tolist()
    cols.pop(0)

    cost = pd.DataFrame(index=rows,columns=['mon','tues','wed','thur','fri'])
    cost = cost.fillna(0)
    

    for i, column in enumerate(cols):

        for row in rows:

            meeting = timetable.loc[row, column]

            if meeting != 0:
                subject = meeting.subject[:-1]
                strack.loc[row, subject] -= 1
            else:
                cost += hc_breached
                continue

            if timetable[column].tolist().count(meeting) > 1: # checks no meetings are scheduled at the same time
                cost += hc_breached

            if (i+1) % 5 == 0: # if it's period 5
                if subject in core_subjects:
                    cost.loc[row, column[0]] += 1

            if skip == False:
                group_subjects = subject_timetable.loc[row].tolist()
                group_subjects = split_list(group_subjects, 5)
                for j, day in enumerate(group_subjects):
                    cost.loc[row, cols[j*5][0]] += len(day) - len(set(day))

        skip = True

    if not strack.eq(0).all().all(): # checks all groups have the right number of meetings per week
        cost += hc_breached

    # if return_df == True:
    #     return cost
    # else:
        
    #     return cost.sum().sum()

    return cost.sum().sum(), cost



def generate_neighboring_solution(timetable, cost):

    rows = timetable.index.tolist()
    columns = timetable.columns.tolist()
    columns.pop(0)

    for row in rows:

        group_meetings = timetable.loc[row, timetable.columns[1:]].tolist()
        group_meetings = split_list(group_meetings, 5)

        weights = cost.loc[row].tolist()

        if sum(weights) == 0:
            weights = [x + 1 for x in weights]

        days = list(Days)
        random_day = random.choices(days, weights)[0]
        day_index = days.index(random_day)
        weights.pop(day_index)
        days.remove(random_day)

        if sum(weights) == 0:
            continue

        random_day2 = random.choices(days, weights)[0]
        
        # now choose a random meeting from each day to swap
        random_day_meetings = group_meetings[Days.index(random_day)]
        random_day_meetings2 = group_meetings[Days.index(random_day2)]
        
        random_period = random.randint(0, len(random_day_meetings) -1)
        random_period2 = random.randint(0, len(random_day_meetings2) -1)

        # if random_day_meetings2[random_period2] not in timetable[(random_day, f'p{random_period + 1}')].tolist():

        #     if random_day_meetings[random_period] not in timetable[(random_day2, f'p{random_period2 + 1}')].tolist():

        #         placeholder = random_day_meetings[random_period]
        #         timetable.loc[row, (random_day, f'p{random_period + 1}')] = random_day_meetings2[random_period2]
        #         timetable.loc[row, (random_day2, f'p{random_period2 + 1}')] = placeholder


        for meeting2 in Meetings[random_day_meetings2[random_period2].subject[:-1]]:
            if meeting2 not in timetable[(random_day, f'p{random_period + 1}')].tolist():
                for meeting in Meetings[random_day_meetings[random_period].subject[:-1]]:
                    if meeting not in timetable[(random_day2, f'p{random_period2 + 1}')].tolist():

                        timetable.loc[row, (random_day, f'p{random_period + 1}')] = meeting2
                        timetable.loc[row, (random_day2, f'p{random_period2 + 1}')] = meeting

    return timetable




def local_search(initial_solution, num_iterations):
    best_solution = initial_solution
    best_solution_copy = best_solution.copy()

    for i in range(num_iterations):

        best_value, value_table = objective_function(best_solution)

        new_solution = generate_neighboring_solution(best_solution_copy, value_table)

        new_value = objective_function(new_solution)[0]

        if new_value < best_value:

            best_solution = new_solution.copy()

    return best_solution

def split_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]



def readable_timetable(table, subject_only=False):
    readable_df = pd.DataFrame()
    readable_df.index = table.index.tolist()
    cols = table.columns.tolist()
    cols.pop(0)

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










best_solution_cost = 99999999
Meetings = createmeetings()


for i in range(3):
    df = create_table()
    df, missing_subjects = assign_meetings()

    run_again = True
    while run_again: # i think i need this loop just in case but potentially can be removed
        df, missing_subjects, run_again  = fill_unfilled_meetings()
        
    current_cost = objective_function(df)[0]
    if current_cost < best_solution_cost:
        best_solution_cost = current_cost
        best_solution = df

    
df = best_solution


# cost_table = objective_function(df)[1]
cost = objective_function(df)[0]


# df = generate_neighboring_solution(df, cost_table)
# cost2 = objective_function(df)[0]
# cost_table = objective_function(df)[1]



df = local_search(df, 10)
print(readable_timetable(df))
print(objective_function(df)[0])
print(f'old values: {cost}')




# print(df)
#df.loc['7N', ('mon','p1')] = 0
#print(missing_subjects)
# print(readable_timetable(True))
# print(objective_function(df))

'''

- check hard constraints of other TT algorithms to make sure i have all of them


'''