def mystery(n) :
    if n <= 0 :
        return 0
    else:
        return n + mystery(n - 1)
#returns 10 because 0+1+2+3+4=10
print(mystery(4))

#another example: 0+1+2....+73 = 2701 
print(mystery(73))
