def main():
    dict_items = {}
    while True:
        try:
            item = input().casefold().upper()
            if item in dict_items:
                dict_items[item] += 1
            else:
                dict_items[item] = 1
            continue

        except EOFError:
            break

    sorted_dict = dict(sorted(dict_items.item()))
    print(sorted_dict)



main()
