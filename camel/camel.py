def main():
    string = input("camelCase: ").strip()
    list = []
    for char in string:
        list.append(char)
        if char.isupper():
            char.replace(char, '_' + char.lower())
            print('snake_case:' list.join())
        else:
            print(list.join())



main()
