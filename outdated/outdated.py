MONTHES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
        date = input('Date: ')
        try:
            list = date.split('/')
            print(list)
            if list:
                year = list[2]
                # print(f'{year}')
                month = MONTHES.index(list[0]) + 1
                print(f'{month}')
                if month < 10:
                    month = '0' + str(month)

                day = list[1]
                if day < 10:
                    day = '0' + str(day)
            # print(f'{year}-{month}-{day}')
            if not list:
                list = date.split(' ')
            break
        except ValueError:
            continue

    print(f'{year}-{month}-{day}')


main()
