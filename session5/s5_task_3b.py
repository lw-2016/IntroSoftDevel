##Find the errors in the following if statements, correct where necessary.
##b)
##if 1 + x > x ** sqrt(2) :
##      y = y + x

#NameError: name 'x' is not defined
#NameError: name 'sqrt' is not defined
#NameError: name 'y' is not defined
import math
x=5
y=7
if 1 + x < x ** math.sqrt(2) :
        y = y + x
        print(y)
  
