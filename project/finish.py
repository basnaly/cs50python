import datetime
from fpdf import FPDF
# pip install fpdf2
import csv
from tabulate import tabulate
import sys
from termcolor import colored, cprint


def finish():

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # Get data from csv file
    data_list, total_sum = get_data()

    pdf = FPDF(orientation='L', unit='mm', format='A5')
    pdf.add_page()

    # Add title
    pdf.set_font('Times', style='', size=24)
    pdf.y = 10
    pdf.cell(text=f'Order from F&V farm', center=True, new_y='TOP')

    # Add date
    pdf.set_font('Times', style='', size=16)
    pdf.y = 25
    pdf.x = 10
    pdf.cell(text=f'Date: {formatted_datetime}', new_x='LEFT', new_y='TOP')

    # Create table
    TABLE_DATA = (
        (product['Name'], product['Price/Kg'], product['Quantity'], product['Sum $']) for product in data_list
    )

    pdf.set_font('Times', size=18)
    pdf.y = 38
    with pdf.table(text_align='CENTER') as table:

        # Create header in table
        row = table.row()
        for datum in ("Product Name", "Price/Kg", "Quantity", "Sum, $"):
            row.cell(datum)

        # Add rows in table
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    # Add total sum
    pdf.set_font('Times', style='B', size=20)
    pdf.y = 85
    pdf.cell(text=f'Total to pay: ${total_sum}', center=False, new_y='TOP')

    pdf.output('order.pdf')
    cprint('Your order was created, see order.pdf file. Thank you!', 'red')


def get_data():
    csv_list = []
    try:
        with open('cart.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                csv_list.append(row)
            # print(tabulate(csv_list, headers="keys", tablefmt="grid"))

            total = 0
            for product in csv_list:
                total += float(product['Sum $'])
            return csv_list, total

    except FileNotFoundError:
        sys.exit('File does not exist')
