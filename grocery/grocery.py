def main():
    dict_items = {}
    while True:
        try:
            item = input().casefold().upper()
            dict_items[item]
            if item in dict_items:
                dict_items[item] += 1
            else:
                dict_items[item] = 1

            print(dict_items)

        except EOFError:
            break



main()
