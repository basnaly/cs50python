from fpdf import FPDF


def main():
    name = input('Name: ')


    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.image(30, 10 name='shirtificate.png', keep_aspect_ratio=True)

    pdf.set_font(family='helvetica', style='', size=40)
    pdf.cell()

    pdf.output('shirtificate.pdf')
