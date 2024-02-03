def main():

    string = input("camelCase: ").strip()
    # Loop on each char in user's string
    # 
    for char in string:
        # If there is an uppercase char in the string
        if char.isupper():
            string = string.replace(char, '_'+ char.lower())
    print(f"snake_case: {string}")


main()
