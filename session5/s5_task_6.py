##7. What do the following nested loops display?  Hand trace. 
##	for i in range(3) :
##      		for j in range(1, 4) :
##           			print(i + j, end="")
##	print()





for i in range(3):
    for j in range(1,4):
        print(i+j, end="")       #adds range i and j in 3 iterations
        print()


print("\n")


for i in range(3):  #gives range 0 1 2
    print(i)


print("\n")

for j in range(1,4):  #gives range 1 2 3
    print(j)
