def mystery(n) :
    if n <= 0 :
        return 0
    else:
        print(n)   # print function to reveal what is going on 
        return n + mystery(n - 1)
        #return n*(n+1)/2  *gauss*

#example function calls
print(mystery(4))
print()
print(mystery(5))
print()
print(mystery(6))
print()
'''
it seems that function  takes paramenter n (for example 4 ),
subtracts 1 from it , takes the result (3) subtracts 1 and so on until it reaches 1
4
3
2
1
and then adds up partial results ==> 4+3+2+1  = 10
'''

# zero returns zero
print(mystery(0))

#negative numbers produce zero
print(mystery(-19))


