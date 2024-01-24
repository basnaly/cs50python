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
                month = MONTHES.index(list[0]) + 1
                if month < 10:
                    month = '0' + str(month)
                day = list[1].replace(',', '')
                if day < 10:
                    day = '0' + str(day)
            else:
                pass
            break

        except ValueError:
            continue

    print(f'{year}-{month}-{day}')
main()
