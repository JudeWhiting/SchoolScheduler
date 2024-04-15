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


def assign_feasible_meetings():   

    rows = df.index.tolist()
    columns = df.columns.tolist()
    columns.pop(0)

    for row in rows:

        subject_tracker = {}    # generate a count of how many subjects are left each loop

        for sub in Subjects:
            subject_tracker[sub.name] = sub.hours

        for column in columns:
            while 1:
                random_meeting = random.choice(Meetings)
                if subject_tracker[random_meeting.subject] != 0:
                    subject_tracker[random_meeting.subject] -= 1
                    break

            df.at[row, column] = random_meeting

    return df



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

            while z < 1000:
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
            
            

    return df

    
    





Meetings = createmeetings()
print(Meetings)
df = create_table()
df = assign_meetings()

print(df)




for i in df[('mon','p5')]:
    print(i.subject)

print()

# prints a whole row
x = df.iloc[0].tolist()
x.pop(0)
for i in x:
    print(i.subject)
#randomly assigns the correct amount of lessons to each student
# hard requirement 1 done YAY

# #df[('mon', 'p1')] = Meeting('eng', Rooms[:4], Teachers[:4], Groups['7N'])
# df.at['7N',('mon','p1')] = 'xD'

# print(df)

# # Get all row labels (index)
# row_labels = df.index.tolist()

# # Get all column labels
# column_labels = df.columns.tolist()
# print(row_labels)
# print(column_labels)

