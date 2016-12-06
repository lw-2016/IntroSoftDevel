##4. Consider this function that
##prints a page number on the left
##or right side of a page:

def main():
    page = int(input("Enter page number: "))
    if page % 2 == 0:
        return True
    
    else:
            print("%60s%d" % (" ", page))




main()

##Introduce a function that returns a Boolean
##to make the condition
##in the if statement easier to understand.
