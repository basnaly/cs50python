def main():
    # Define dict of items
    dict_items = {}
    while True:
        try:
            # Convert user's input to insensitively case with uppercase chars
            item = input().casefold().upper()
            if item in dict_items:
                # Add 1 to a count of the same word
                dict_items[item] += 1
            else:
                # Set
                dict_items[item] = 1
            continue

        except EOFError:
            break

    # Sort the dict alphabetically
    # From: https://www.freecodecamp.org/news/python-sort-dictionary-by-key/
    sorted_dict = dict(sorted(dict_items.items()))
    for item in sorted_dict:
        print(f'{sorted_dict[item]} {item}')


main()
