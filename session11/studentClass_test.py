from studentClass import *

# 5 EXAMPLES OF OBJECTS
s1 =Student("Wilk", "Lukas", "21007619","Computer Science With Foundation")
s2=Student("Smith", "Stephan", "21001723","Japanese Literature")
s3=Student("Doe", "John", "21001723","Applied Methodology")
s4=Student("Carmichael", "Monica", "21001723","Quantum Physics Without Foundation")
s5=Student("Morty", "Rick", "21001723","Pure Statistical Analysis")

#==TEST1 ==(testing getters) based on s1 object example
print("==Test_1 student object s1 existing information==: ")
s1.getSurname()
s1.getName()
s1.getStudentNumber()
s1.getStudentCourse()
print()

#==TEST2 ==(testing setters)
#1 informatrion before: "Doe", "John", "21001723","Applied Methodology"
print("==Test_2 to set new information about student s3==")
print("Information before:")
s3.studentInfo()
print()
#2 change student info (testing setters)
print("Information changed to:")
s3.setSurname("Lee")
s3.setName("Jerry")
s3.setStudentNumber(21007777)
s3.setStudentCourse("Sound Engineering")

#3 information after: Lee Jerry 21007777 Sound Engineering
print()
print("Now student s3 information is changed: ")
s3.studentInfo()



