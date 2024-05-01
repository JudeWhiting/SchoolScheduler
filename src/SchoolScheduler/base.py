import pandas as pd
import numpy as np
import copy
import random




# Declaration of all global variables
Days = ['mon','tues','wed','thur','fri']
core_subjects = ['eng','math','phy','bio','chem']
Subjects = []
Teachers = []
Classrooms = []
Students = []
Meetings = []




# asks the user to input how many classes there should be in each group and how long they want the program to take
while 1:

    try:

        classes_per_group = int(input('How many sets are there per group?\n>  '))
        time_taken = input('Enter a number to select how long the algorithm takes (more slow = more optimised): 1 for fast, 2 for medium, 3 for slow, 4 for very slow\n>  ')
        epochs_dic = {'1': 10,
                      '2': 30,
                      '3': 50,
                      '4': 100}
        epochs = epochs_dic[time_taken]

        break

    except:

        input('Please enter a number!')




class Subject:

    def __init__(self, name, hours):

        self.name = name
        self.hours = int(hours)




class Teacher:

    def __init__(self, name, classroom, subjects=[]):

        self.name = name
        self.classroom = classroom
        self.subjects = subjects




class Student:

    def __init__(self, name, group, sets):

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




class Meeting:

    def __init__(self, subject, teachers):

        self.subject = subject
        self.teachers = teachers