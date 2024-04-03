import pandas as pd
import numpy as np

class Teacher:

    teacher_count = 0

    def __init__(self, name, subjects=[]):

        self.ID = Teacher.teacher_count
        self.name = name
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

    def __init__(self, name, year):

        self.ID = Student.student_count
        self.name = name
        self.year = year

        Student.student_count += 1



class Meeting:

    def __init__(self, ID, students, teacher, subject, room):
        pass


Subjects = []
Teachers = []
Rooms = []
Students = []

with open ('src/data/teachers.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' , ')
        Teachers.append(Teacher(parts[0], parts[1:]))

with open ('src/data/students.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(', ')
        Students.append(Student(parts[0], parts[1]))

with open ('src/data/rooms.txt') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' , ')
        Rooms.append(Room())

data = {
    ('main', 'student'): Students
}

df = pd.DataFrame(data)
for day in ['mon','tues','wed','thur','fri']:

        for i in range(1,6):

            df[(day, f'p{i}')] = np.zeros(len(Students))

print(df)

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


