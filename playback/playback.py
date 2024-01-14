# Define the main function
def main():
    # Ask user to type a sentence and save it to a list variable
    list = input("Type a sentence ").split(' ')

    # Convert the list to the string with
    string = '...'.join(list)
    print(string)


main()
