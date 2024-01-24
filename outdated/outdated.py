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
    date = input('Date: ')
    while True:
        try:
            list = date.split('/')
            if list:
                year = list[2]
                print(f'{year}')
                month = MONTHES.index(list[0]) + 1
                if month < 10:
                    month = '0' + str(month)
                    print(f'{month}')
                #day = list[1]
            #     if day < 10:
            #         day = '0' + str(day)
            # print(f'{year}-{month}-{day}')
            if not list:
                list = date.split(' ')
            break
        except ValueError:
            continue

    # print(f'{year}-{month}-{day}')


main()
