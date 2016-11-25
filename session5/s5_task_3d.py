##Find the errors in the following if statements, correct where necessary.
##


 #NameError: name 'grade' is not defined

grade = 90#assign value of 90 as an example
if grade >= 90 :
    letterGrade = "A" #elif was missing
elif grade >= 80 :
    letterGrade = "B"
elif grade >= 70 :
    letterGrade = "C"
elif grade >= 60 :
    letterGrade = "D"
else:
    letterGrade = "F" 
print (letterGrade)





