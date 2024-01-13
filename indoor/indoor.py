# define the main function
def main():
    # Ask user for prompt
    voice = input("")

    # if user prompt typed lowercase string, print the string in upper case
    if voice.islower():
        print(voice.upper())

    # if user prompt typed uppercase string, print the string in lower case
    else:
        print(voice.lower())


main()
