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
            if len(list) == 3: # 7/9/1234
                year = list[2]
                print(f'{year}')
                month = int(list[0])
                if month < 10:
                    month = '0' + str(month)
                print(f'{month}')
                day = int(list[1])
                if day < 10:
                    day = '0' + str(day)
            print(f'{year}-{month}-{day}')
            if date[0].isalpha(): # September 8, 1636
                list = date.split(' ')
                year = list(2)
                month = MONTHES.index(int(list[0]))
            break
        except ValueError as e:
            print('cdf', e)
            continue

    print(f'{year}-{month}-{day}')


main()
