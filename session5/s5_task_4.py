#ask user for input
richter_mag = float(input("Please enter the magnitude on Richter scale (between 0-8.0): ")) 


#if-elif-else flow control structure
if richter_mag >= 8.0:                                                            
	print("most structures fall")
elif richter_mag >= 7.0:
	print("many buildings destroyed")
elif richter_mag >= 6.0:
	print("many buildings considerably damaged, some collapse")
elif richter_mag >= 4.5:
	print("damage to poorly constructed buildings")
else:
	print("no destruction of buildings")
