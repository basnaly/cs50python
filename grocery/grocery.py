def main():
    dict_items = {}
    while True:
        try:
            item = input().casefold().upper()
            dict_items[item] = item
            print(dict_items)

        except EOFError:
            break



main()
