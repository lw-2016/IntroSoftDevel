class Student()  :

    def __init__ (self, surname, name, student_number, student_course):
        self._surname   =   surname
        self._name        =  name
        self._number    =   student_number
        self._course     =   student_course

    def getSurname(self):
        print(self._surname)
        return (self._surname)
    
    def setSurname(self, surname):
        self._surname=surname
        print(self._surname)
        
    def getName(self):
        print(self._name)
        return (self._name)
    
    def setName(self,name):
        self._name=name
        print(self._name)
        
    def getStudentNumber(self):
        print(self._number)
        return (self._number)
    
    def setStudentNumber(self,number):
        self._number=number
        print(self._number)
        
    def getStudentCourse(self):
        print(self._course)
        return (self._course)
    
    def setStudentCourse(self,course):
        self._course=course
        print(self._course)

    #method to enable get all information combined about students
    def studentInfo(self):
        print(self._surname, self._name, self._number, self._course)
        return self._surname, self._name, self._number, self._course
        
