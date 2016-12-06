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

#create dictionary which counts word occurrences
print()
print("Here are your words together with occurrences:")
for item in spl:
    dictio={item : spl.count(item)}
    print(dictio)

#prints each item from dictionary
print()
print("Here is each item from your input:")
for item in range(len(spl)) :
    print( spl[item])
    
