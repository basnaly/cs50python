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

    # From: https://www.freecodecamp.org/news/python-sort-dictionary-by-key/
    sorted_dict = dict(sorted(dict_items.items()))
    for item in sorted_dict:
        print(f'{sorted_dict[item]} {sorted_dict}')


main()
