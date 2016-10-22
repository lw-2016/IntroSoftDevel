#Consider the following code:

x = 19.93
y = 20.00
z = y - x
print(z)

#The output is 0.0700000000028    Why is that so?   
#mprove the code so that the output is to two decimal places.


#improved version returns output to two decimal places.
x = 19.93
y = 20.00
z = y-x

print("%.2f" % z)
