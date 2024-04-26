from Base import *

with open ('src/data/groups.txt', 'r') as file:
    Groups = {}
    for line in file:
        line = line.strip()
        Groups[line] = []


with open ('src/data/teachers.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' , ')
        Teachers.append(Teacher(parts[0], parts[1], parts[2:]))

with open ('src/data/students.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' , ')
        student = Student(parts[0], parts[1], [int(x) for x in parts[2:]])
        Groups[student.group].append(student)
        Students.append(student)
        


with open ('src/data/subjects.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' , ')
        subject = Subject(parts[0], parts[1])
        Subjects.append(subject)

