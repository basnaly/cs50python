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
        date = input('Date: ').strip()
        try:
            list = date.split('/')
            if len(list) == 3: # 7/9/1234
                year = list[2]

                month = int(list[0])
                if month > 12:
                    continue
                if month < 10:
                    month = '0' + str(month)

                day = int(list[1])
                if day > 31:
                    continue
                if day < 10:
                    day = '0' + str(day)

            elif date[0].isalpha(): # September 8, 1636
                list = date.split(' ')
                year = list[2]

                month = MONTHES.index(list[0]) + 1
                if month > 12:
                    continue
                if month < 10:
                    month = '0' + str(month)

                day = list[1]
                print(day[1])
                if day[1] == '':
                    continue
                day = int(list[1].replace(',', ''))
                if day > 31:
                    continue
                if day < 10:
                    day = '0' + str(day)
            else:
                continue

            break

        except ValueError:
            continue

    print(f'{year}-{month}-{day}')


main()
