from Base import *
from Read_Files import *
df = pd.DataFrame()

def create_table():
    data = {
        ('main', 'group'): Groups
    }

    df = pd.DataFrame(data)

    for day in Days:
        for i in range(1,6):

            df[(day, f'p{i}')] = np.zeros(len(Groups))    # assign_meetings()

    return df
    


def create_meetings():

    chosen_teachers = {}
    chosen_rooms = {}
    Meetings = []

    for sub in Subjects:

        teachers_with_matching_subject = [teacher for teacher in Teachers if sub.name in teacher.subjects]
        classrooms_with_matching_subject = [classroom for classroom in Classrooms if classroom.block == sub.name]
        chosen_teachers[sub.name] = []
        chosen_rooms[sub.name] = []

        for i in range(4):

            chosen_teachers[sub.name].append(random.choice(teachers_with_matching_subject))
            chosen_rooms[sub.name].append(random.choice(classrooms_with_matching_subject))

    for sub in Subjects:
        Meetings.append(Meeting(sub.name, chosen_rooms[sub.name], chosen_teachers[sub.name]))

    return Meetings

def createmeetings():

    Meetings = {}

    for sub in Subjects:

        Meetings[sub.name] = []

        teachers_with_matching_subject = [teacher for teacher in Teachers if sub.name in teacher.subjects]
        for i in range(int(len(teachers_with_matching_subject) / classes_per_group)):

            Meetings[sub.name].append(Meeting(f'{sub.name}{i+1}', [teacher.classroom for teacher in teachers_with_matching_subject], teachers_with_matching_subject[i*classes_per_group : classes_per_group + i*classes_per_group]))

    return Meetings



def assign_meetings():    # needs to return an array of meetings

    rows = df.index.tolist()
    columns = df.columns.tolist()
    columns.pop(0)


    # creates the amount of hours per subject per week needed
    strack = pd.DataFrame()
    strack.index = df.index.tolist()
    for sub in Subjects:
        strack[sub.name] = sub.hours

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

    

    return df
                                












Meetings = createmeetings()
print(Meetings)
df = create_table()
df, missing_subjects = assign_meetings()

print(df)
print(missing_subjects)
df = fill_unfilled_meetings() # need to test
print(df)





# prints a whole column
for i in df[('fri','p5')]:
    if i == 0:
        print(0)
        continue
    print(i.subject)
print()

# prints a whole row
x = df.iloc[9].tolist()
x.pop(0)
for i in x:
    if i == 0:
        print(0)
        continue
    print(i.subject)


