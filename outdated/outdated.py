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
            date_list = date.split('/')
            if len(date_list) == 3:
                

        except ValueError:
            continue

    print(f'{year}-{month}-{day}')


main()
