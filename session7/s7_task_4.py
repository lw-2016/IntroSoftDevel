#construct function 
def main():   
    page = 555  #odd page number
# if page number is even, function returns Boolean True

    if page % 2 == 0:  
         print(page,True)
         return True
# if page number is odd, function returns Boolean False 
    else:
            print("%60s%d" % (" ", page),False) 
            return False


main() #call function


