#Explain the mistake in the following code:
#radius = input(float("Enter the radius:"))


#should be float(input... not input(float..
radius = float(input("Enter the radius:"))
