##5.Transform the following instructions
##into a function called count_spaces.
##Define a main function that
##will ask the user to enter some input
##and call the count_spaces function to
##return the number of spaces.




# Counts the number of spaces
userInput  =  input("enter: ")
spaces = 0
for char in userInput :
    if char == " " :
        spaces = spaces + 1
print(spaces)
