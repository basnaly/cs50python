from fpdf import FPDF


def main():
    name = input('Name: ')


    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.image(30, 10 name='shirtificate.png', keep_aspect_ratio=True)

    pdf.set_font(family='helvetica', style='', size=40)
    pdf.y = 40
    pdf.cell(text='CS50 Shirtificate', center=True, new_y='TOP')

    pdf.output('shirtificate.pdf')


main()
