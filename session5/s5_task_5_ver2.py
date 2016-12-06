#version2 limiting user input to 5 attempts:

#declare variable passwd 
passwd="changeme"

count=0              #count from 0
while count <5:  #condition is that it  must be 5 times
    count=count+1     #counting increase by one

    #prompt user for input
    userInput=input("Please enter \"changeme\" to change your password: ")

    #first decision: if user inputs right password:accept
    if userInput == passwd:
        print("\n\nAccepted on", count, "attempt")
        break # use break otherwise program asks again for password even if user inputs right one.

    #second decision: if user inputs wromg password : deny
    if userInput !=passwd:
        print("Wrong password")

    #third decision: if user reaches fifth try without providing right password inform him that
    #this was his last attempt
        
    if count==5:
            print("""\n*** ***access denied, please press enter to exit
and contact security to reset your password*** ***\n""")

            input()  # waits for user to exit program by pressing enter



