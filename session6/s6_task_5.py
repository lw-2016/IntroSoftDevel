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
x.sort()
print("sort alphabetically: ", x, "\n")

#total number of words
print ("you have entered in total " , len(x), "words \n")


a1=a
a1=dict([i, a1.count(i)] for i in a1)
print(a1)
           





for i in x:
    print (i, "=", x.count(i))







print()
for i in range(len(x)) :
    print(i, x[i])

    
'''
for i in range(len(x)):
    print (i, x.count(1))
    
x=x.count(x)
print(x)

for i in a:
    print (i,a[i])


print("\n")
print("print each item:\n")
#print each item from dictionary
i=1
for i in x:
    print (i)
    i+=1




'''
