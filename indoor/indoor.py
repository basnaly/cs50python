# define the main function
def main():
    # Ask user for the prompt
    voice = input("")

    # if user typed lowercase string, print the string in upper case
    if voice.islower():
        print(voice.upper())

    # if user typed uppercase string, print the string in lower case
    else:
        print(voice.lower())


main()
