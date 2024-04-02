class Teacher:


    def __init__(self, ID, name, subjects=[]):

        self.ID = ID
        self.name = name
        self.subjects = subjects


if __name__ == "__main__":

    # teacher0 = Teacher(0, 'A. Johnson', ['english'])
    # print(Teacher.all_instances[0].name)

    Teachers = []
    Teachers.append(Teacher(len(Teachers), 'A. Johnson', ['eng', 'ict']))
    Teachers.append(Teacher(len(Teachers), 'B. Bryson', ['math']))
    print(Teachers[1].name)