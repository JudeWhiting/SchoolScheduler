import pandas as pd

class Teacher:

    def __init__(self, ID, name, subjects=[]):

        self.ID = ID
        self.name = name
        self.subjects = subjects

class Room:
    def __init__(self, ID, name, block):

        self.ID = ID
        self.name = name
        self.block = block

class Student:

    def __init__(self, ID, name, year):

        self.ID = ID
        self.name = name
        self.year = year

class Meeting:

    def __init__(self, ID, students, teacher, subject, room):
        pass



data = {
    ('main', 'class'): ['c1','c2','c3','c4'],
    ('monday', 'p1'): [0,0,0,0],
    ('monday', 'p2'): [0,0,0,0],
    ('monday', 'p3'): [0,0,0,0],
    ('monday', 'p4'): [0,0,0,0],
    ('monday', 'p5'): [0,0,0,0]
}

df = pd.DataFrame(data)
print(df)


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


# Teachers = []
# Teachers.append(Teacher(len(Teachers), 'A. Johnson', ['eng', 'ict']))
# Teachers.append(Teacher(len(Teachers), 'B. Bryson', ['math']))
# print(Teachers[1].name)