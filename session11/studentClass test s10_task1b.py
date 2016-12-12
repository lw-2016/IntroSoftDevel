from studentClass_task1a import *

# 5 EXAMPLES OF OBJECTS
s1 =Student("Wilk", "Lukas", "21007619","Computer Science With Foundation")
s2=Student("Smith", "Stephan", "21001723","Japanese Literature")
s3=Student("Doe", "John", "21001723","Applied Methodology")
s4=Student("Carmichael", "Monica", "21001723","Quantum Physics Without Foundation")
s5=Student("Morty", "Rick", "21001723","Pure Statistical Analysis")

#==TEST1 ==(testing getters) based on s1 object example
s1.getSurname()
s1.getName()
s1.getStudentNumber()
s1.getStudentCourse()
print()

#==TEST2 ==(testing setters)
#1 informatrion before: "wilk", "lukas", "21007619","Computer Science With Foundation"
s1.studentInfo()
print()
#2 change student info (testing setters)
s1.setSurname("Lee")
s1.setName("Jerry")
s1.setStudentNumber(21007777)
s1.setStudentCourse("Sound Engineering")

#3 information after: Lee Jerry 21007777 Sound Engineering
print()
s1.studentInfo()

#summary: method studentInfo() prints out all student information of all students.
print()
s1.studentInfo()
s2.studentInfo()
s3.studentInfo()
s4.studentInfo()
s5.studentInfo()


