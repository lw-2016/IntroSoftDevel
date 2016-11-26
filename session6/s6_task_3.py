#3.What is the output? 

nums = []
for x in [1,2,3]:
         for y in [3,1,4]:#nested loop for inside another for loop
                if x != y:
                        nums.append((x,y))
print(nums)




