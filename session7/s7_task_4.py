##4. Consider this function that
##prints a page number on the left
##or right side of a page:


if page % 2 == 0:
    print(page)
else:
    print("%60s%d" % (" ", page))




##Introduce a function that returns a Boolean
##to make the condition
##in the if statement easier to understand.
