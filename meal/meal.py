def main():
    time = input("What time is it? ")
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

    hours, minutes = time.split(':')
    converted_time = float(hours) + float(minutes) / 60
    return converted_time



if __name__ == "__main__":
    main()
