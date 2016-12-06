#function main
def main():
    #promt user for input
    userInput = input("Enter sentence and I will count spaces for You: \n\n")
    print(count_spaces(userInput))


#function count_spaces
def count_spaces(userInput):
    # Counts the number of spaces
    spaces = 0
    #for loop to check how many spaces user has entered
    for char in userInput :
        if char == " ":
            spaces = spaces + 1
    return spaces

main()
