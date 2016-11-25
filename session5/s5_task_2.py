##2. Supply a condition in this if statement to test if the user entered a “Y”:
##	userInput = input("Enter Y to quit.")
##	if . . . // supply statement
##		print("Goodbye")    // if the user entered “Y”

while True:
    userInput = input("Enter Y to quit.")
    if userInput == "Y":
        print("Goodbye")
    else:
        print ("Error: You did not enter capital \"Y\".Please Try Again...")
