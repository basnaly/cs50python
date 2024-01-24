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
            if len(list) == 3:
                year = list[2]
                print(f'{year}')
                month = list[0]
                print(f'abc {month}')
                if month < 10:
                    month = '0' + str(month)

                day = list[1]
                if day < 10:
                    day = '0' + str(day)
            # print(f'{year}-{month}-{day}')
            if not list:
                list = date.split(' ')
            break
        except ValueError as e:
            print('cdf', e)
            continue

    print(f'{year}-{month}-{day}')


main()
