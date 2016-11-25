##1. What is the error in this statement?
##	if scoreA = scoreB :
##        		print("Tie")

scoreA=5
scoreB=5
if scoreA == scoreB :
    print("Tie")

##1.invalid syntax
##2.NameError: name 'scoreA' is not defined
##3.NameError: name 'scoreB' is not defined

# as expected does not print Tie because scoreA is not equal to scoreB
scoreA=5
scoreB=9
if scoreA == scoreB :
    print("Tie")
