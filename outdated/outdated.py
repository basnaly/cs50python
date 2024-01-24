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
            if len(list) == 3: # 7/9/1234
                year = list[2]
                month = int(list[0])
                if month < 10:
                    month = '0' + str(month)
                day = int(list[1])
                if day < 10:
                    day = '0' + str(day)
            if date[0].isalpha(): # September 8, 1636
                list = date.split(' ')
                year = list[2]
                month = MONTHES.index(list[0]) + 1
                if month < 10:
                    month = '0' + str(month)
                day = int(list[1].replace(',', ''))
                if day < 10:
                    day = '0' + str(day)
            break
        except ValueError:
            continue

    print(f'{year}-{month}-{day}')


main()
