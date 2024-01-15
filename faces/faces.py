# Define convert function that gets str
def convert(str):
    # Convert str using replace() function
    return str.replace(":)", "🙂").replace(":(", "🙁")

# Define main function
def main():
    # Prompt user to type str (string)
    str = input("")
    # Print converted str
    print(convert(str))


main()
