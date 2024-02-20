from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image('shirtificate.png', 20, 80, 170, keep_aspect_ratio=True)

pdf.set_font('helvetica', 'B', 40)
pdf.y = 40
pdf.cell(text='CS50 Shirtificate', new_x="LMARGIN", new_y="TOP", center=True)
pdf.output('shirtificate.pdf')
