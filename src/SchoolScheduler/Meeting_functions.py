from Base import *


# 



def create_meetings(Subjects, Classrooms, Teachers):

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

Meetings = create_meetings(Subjects, Rooms, Teachers)


rows = df.index.tolist()
columns = df.columns.tolist()
columns.pop(0)

def sub_track(subs):
    subject_tracker = {}
    for sub in subs:
        subject_tracker[sub.name] = int(sub.hours)
    return subject_tracker

for row in rows:
    subject_tracker = sub_track(Subjects)
    for column in columns:
        while 1:
            random_meeting = random.choice(Meetings)
            if subject_tracker[random_meeting.subject] != 0:
                subject_tracker[random_meeting.subject] -= 1
                break

        df.at[row, column] = random_meeting


print(df)
print(subject_tracker)

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