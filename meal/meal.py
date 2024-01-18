def main():
    time = input("What time is it? ")
    # Call convert function with agrument of user's input
    digital_time = float(convert(time))
    if 7 <= digital_time <= 8:
        print('breakfast time')
    elif 12 <= digital_time <= 13:
        print('lunch time')
    elif 18 <= digital_time <= 19:
        print('dinner time')
    else:
        print('', end='')


def convert(time):
    # Split user's input by ':'
    hours, minutes = time.split(':')
    # Convert the time format into a digital format
    converted_time = float(hours) + float(minutes) / 60
    return converted_time


if __name__ == "__main__":
    main()
