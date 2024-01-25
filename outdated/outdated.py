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
        # Remove spaces in user's input
        date = input('Date: ').strip()
        try:
            # Split date string by '/'
            date_list = date.split('/') #9/8/1636

            if len(date_list) == 3:
                
                year = date_list[2] # '1636'

                month = int(date_list[0]) # 9
                if month > 12:
                    continue
                if month < 10:
                    month = '0' + str(month)

                day = int(date_list[1]) # 8
                if day > 31:
                    continue
                if day < 10:
                    day = '0' + str(day)
                break

            elif len(date_list) == 1: # September 8, 1636
                date_list = date.split(' ')

                year = date_list[2] # '1636'

                month = MONTHES.index(date_list[0]) + 1
                if month > 12:
                    continue
                if month < 10:
                    month = '0' + str(month)

                day = date_list[1] # '8,'

                if len(day) == 1:
                    continue
                else:
                    day = int(day.replace(',', ''))
                    if day > 31:
                        continue
                    if day < 10:
                        day = '0' + str(day)
                break
            else:
                continue

        except ValueError:
            continue

    print(f'{year}-{month}-{day}')


main()
