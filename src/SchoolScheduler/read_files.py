from base import *
while 1:
    try:
        dataset = input(f'Which dataset would you like to use? 1 or 2\n>  ')
        datasets = {'1' : '',
                    '2' : '2'}
        dataset = datasets[dataset]
        break
    except:
        input('Please enter  a valid choice!')


# creates a dictionary with keys corresponding to group names
with open (f'src/data/groups{dataset}.txt', 'r') as file:
 
    Groups = {}

    for line in file:

        line = line.strip()
        Groups[line] = []




# the code below reads each input file and puts the information on each line into an instance of the files' corresponding class
# each instance is then appended to a list of its corresponding class




with open (f'src/data/teachers{dataset}.txt', 'r') as file:

    for line in file:

        line = line.strip()
        parts = line.split(' , ')

        Teachers.append(Teacher(parts[0], parts[1], parts[2:]))




with open (f'src/data/students{dataset}.txt', 'r') as file:

    for line in file:

        line = line.strip()
        parts = line.split(' , ')

        student = Student(parts[0], parts[1], [int(x) for x in parts[2:]])

        Groups[student.group].append(student)
        Students.append(student)
        



with open (f'src/data/subjects{dataset}.txt', 'r') as file:

    for line in file:

        line = line.strip()
        parts = line.split(' , ')

        subject = Subject(parts[0], parts[1])

        Subjects.append(subject)