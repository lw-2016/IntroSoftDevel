#version1

#declare variable
passwd = "changeme"

#prompt user for input and count attempts
count=0
while True:
    userInput=input("Please enter \"changeme\" to change your password: ")
    count=count+1 #count attempts
    
    #decion1: in case user inputs wrong password inform him about it.
    if userInput != passwd:
        print("wrong password")

    #desion2: if user inputs correct password print accepted and display how many attempts
    if userInput == passwd:
        print("Accepted on", count , "attempt")
        break # stop asking if password is correctly entered.

