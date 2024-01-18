def main():
    digital_time = convert(time)
    if 7 <= digital_time >= 8:
        print('breakfast time')
    elif 12 <= digital_time >= 13:
        print('lunch time')
    elif 18 <= digital_time >= 19:
        print('dinner time')
    else:
        print('', end='')


def convert(time):
    time = input("What time is it? ")
    hours, minutes = time.split(':')
    converted_time = float(hours) + float(minuts) / 60
    return converted_time



if __name__ == "__main__":


main()
