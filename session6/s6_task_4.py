shoppingList = [] #empty list
userInput = input ("Pleae enter your product \n") #ask user for input

while (userInput != ""):
    shoppingList.append(userInput)  #add items to list
    userInput = input("Pleae enter your product:\n")



#print list in easy to read format
print("Thank you for shopping")
print ("this is your shopping list: \n")

for i in shoppingList:
    print("***",i,"***")
    
      
