import pandas as pd
import numpy as np
import copy
import random

Days = ['mon','tues','wed','thur','fri']
# Groups = {'7N':[],'7S':[],
#           '8N':[],'8S':[],
#           '9N':[],'9S':[],
#           '10N':[],'10S':[],
#           '11N':[],'11S':[]
#           }

Subjects = []
Teachers = []
Classrooms = []
Students = []
Meetings = []
core_subjects = ['eng','math','phy','bio','chem']
#epochs = 10

while 1:
    try:
        classes_per_group = int(input('How many classes are there per group?\n>  '))
        break
    except:
        input('Please enter a number!')

class Subject:

    subject_count = 0

    def __init__(self, name, hours):

        self.ID = Subject.subject_count
        self.name = name
        self.hours = int(hours)

        Subject.subject_count += 1


class Teacher:

    teacher_count = 0

    def __init__(self, name, classroom, subjects=[]):

        self.ID = Teacher.teacher_count
        self.name = name
        self.classroom = classroom
        self.subjects = subjects

        Teacher.teacher_count += 1

class Room:

    room_count = 0

    def __init__(self, name, block):

        self.ID = Room.room_count
        self.name = name
        self.block = block

        Room.room_count += 1

class Student:

    student_count = 0

    def __init__(self, name, group, sets):

        self.ID = Student.student_count
        self.name = name
        self.group = group
        self.sets = {
            'tut' : sets[0],
            'eng' : sets[1],
            'math' : sets[2],
            'chem' : sets[3],
            'phy' : sets[3],
            'bio' : sets[3]
        }

        Student.student_count += 1



class Meeting:

    meeting_count = 0

    def __init__(self, subject, teachers):

        self.ID = Meeting.meeting_count
        self.subject = subject
        self.teachers = teachers

        Meeting.meeting_count += 1






# create table




# Teachers = []
# Teachers.append(Teacher(len(Teachers), 'A. Johnson', ['eng', 'ict']))
# Teachers.append(Teacher(len(Teachers), 'B. Bryson', ['math']))

# Rooms = []
# Rooms.append(Room(len(Rooms), 'm1', 'math'))
# Rooms.append(Room(len(Rooms), 'e1', 'eng'))
# Rooms.append(Room(len(Rooms), 'c1', 'ict'))

# Students = []
# Students.append(Student('J. Whiting', 7))
# Students.append(Student('B. Butten', 8))
# Students.append(Student('H. Castley', 9))
# Students.append(Student('H. Philippi', 10))





# print(df[('main','student')][3].ID)
# print()

# # Create a DataFrame with a MultiIndex column
# data = {
#     ('Main', 'Name'): ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#     ('Main', 'Age'): [25, 30, 35, 40, 45],
#     ('Sub', 'Gender'): ['Female', 'Male', 'Male', 'Male', 'Female'],
#     ('Sub', 'Country'): ['USA', 'Canada', 'UK', 'Australia', 'Japan']
# }
# df = pd.DataFrame(data)

# # Display the DataFrame
# print("DataFrame with sub-columns:")
# print(df)






# print(df)
# print(df.iloc[2])
# print(df[df['Age'] > 30])
# print(df.sort_values(by='Age', ascending=False))


