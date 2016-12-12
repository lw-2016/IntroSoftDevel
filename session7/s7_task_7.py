def mystery(n) :
    if n <= 0 :
        return 0
    else:
        print(n) #use print (n) to reveal what function does here
        return mystery(n // 2) + 1 # +1 seems to do count it does not add 1 to n//2

print(mystery(20)) 
print()

'''
function accepts first parameter for example 20 ,
shows how many times 2 fits into 20 (it is 10 because(20//2=10))
then takes that result and shows how many times 2 fits in 10 in this case 5
and repeat recursively this operation untit exhausts possibilities
then returns count of how many operations it performed)
in this case  parameter was 20 so it is 5 operations.
1.   20
2.   10
3.    5
4.    2
5.    1
'''
#few more examples
print ("more examples: \n")
print(mystery(8))
print()
print(mystery(16))
print()
print(mystery(32))











