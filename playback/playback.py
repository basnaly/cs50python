# Define the main function
def main():
    # Ask user to type a sentence, convert it to a list and save it
    list = input("Type a sentence ").split(' ')

    # Convert the list to the string adding 3 dots between the words
    string = '...'.join(list)
    print(string)


main()
