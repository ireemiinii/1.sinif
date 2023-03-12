class student:
    def __init__(self, studentID, name, totalCredits, **kwargs):
        self.studentID = studentID
        self.name = name
        self.totalCredits = totalCredits
        self.__dict__.update(kwargs)

    def takeCourse(self, course):
        course.studentEnrolled(self)
        self.totalCredits += course.credit
        course.studentslist.append(self.studentID)

    def dropCourse(self, course):
        if (self.studentID not in course.studentslist):
            return print("cannot drop it")
        
        x = str(input("Dear Prof. {} \n" \
                  "The student {} wants to drop your course: \n"\
                  "{}\n"\
                  "Is it ok? (y/n):  "\
                  .format(course.instructor.name, self.name, course.name)))
        if(x == "n"):
                print("there is no approve")
                
        else:
            print(self.studentID)
            course.studentslist.remove(self.studentID)
            print(course.studentslist)
            course.numEnrolled -=1
            course.instructor.totalStudents -=1

class courses:
    def __init__(self, code, name, credit, instructor):
        self.code = code
        self.name = name
        self.credit = credit
        self.numEnrolled = 0
        self.instructor = instructor
        self.studentslist = []
        

    def getStudentlist(self):
        getStudentlistparameter = self.numEnrolled
        print(self.studentslist)
           


    
    def studentEnrolled(self, student):

        self.numEnrolled += 1
        self.informInstructor(student)

    def informInstructor(self, student):
        self.instructor.totalStudents += 1

        message = "Dear Prof. {} \n" \
                  "The student {} has taken your course: \n"\
                  "{}".format(self.instructor.name, student.name, self.name)
        print(message)
        

class instructor:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.totalStudents = 0

prof1 = instructor('Berk', 'banbar@hacettepe.edu.tr')
prof2 = instructor('Hayrettin', 'kral06@hacettepe.edu.tr')
course1 = courses('GMT 104', 'Intro to Programming-II', 6, prof1)
course2 = courses('GMT 112', 'Intro to Cevdet reyiz', 6,prof1)
course3 = courses('GMT 342', 'bursadangelengolhaberi', 6,prof2)
student1 = student(123, 'Ali', 35, email='ali@hacettepe.edu.tr', hobby='football')
student2 = student(151, 'Alex', 30)
print(student1.__dict__)

student1.takeCourse(course1)
print(prof1.totalStudents)
