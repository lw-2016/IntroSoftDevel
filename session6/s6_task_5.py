#ask user for input
a=str(input ("Please write whatever  is on your mind: "))
b=str(input(" One more statement , please:"))
print()

#concatenate input
concat = a+ " " +b
print ("concatenate:" ,concat,"\n")

#split sentences from list of words
spl=concat.split()
print("split: ", spl, "\n")

#sort
spl.sort()
print("sort alphabetically: ", spl, "\n")

#total number of words
print ("You have entered in total " , len(spl), "words \n")
print()

#create dictionary, which counts word occurrences
dictio=dict()
for key in spl:
    dictio[key]=spl.count(key)
print("Here are dictionary of words together with occurrences:",dictio)
print()

#prints each item from dictionary
print("This is list of dictionary keys entered: ")
for i in dictio:
    print(i)




    
