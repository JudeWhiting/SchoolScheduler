class Classes:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name


class Teachers:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

class Rooms:
    def __init__(self, ID, name):
        

class Courses(Classes, Teachers):
    def __init__(self, courseID, classID, teacherID, subject_name, number_of_lessons):
        self.courseID = courseID
        self.classID = classID
        self.teacherID = teacherID
        self.subject_name = subject_name
        self.number_of_lessons = number_of_lessons



if __name__ == "__main__":
    

