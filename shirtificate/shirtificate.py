from fpdf import FPDF


def main():
    name = input('Name: ')


    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.image('shirtificate.png', 10, 70, 190, keep_aspect_ratio=True)

    pdf.set_font(family='helvetica', style='', size=40)
    pdf.y = 40
    pdf.cell(text='CS50 Shirtificate', center=True, new_y='TOP')

    pdf.set_font(family='helvetica', style='', size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.y = 130
    pdf.cell(text=name + ' took CS50', center=True, new_y='TOP')

    pdf.output('shirtificate.pdf')


main()
