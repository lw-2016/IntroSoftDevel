#ask user for input
a=input ("please write whatever  is on your mind: ")
b=input(" one more statement , please:")
print("\n")
#concatenate input
x = a+ " " +b
print ("concatenate:" ,x,"\n")

#split sentences from list of words
x=x.split()
print("split: ", x , "\n")


#sort
x.sort
print("sort alphabetically: ", x, "\n")

#total number of words
print ("you have entered in total " , len(x), "words \n")



i=1
for i in range (len(x)):
    i=i+1
    print(i,{})
    



    


'''
print("\n")
print("print each item:\n")
#print each item from dictionary
i=1
for i in x:
    print (i)
    i+=1

'''


