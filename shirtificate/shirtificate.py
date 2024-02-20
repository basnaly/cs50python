from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image('shirtificate.png', 20, 80, 170, keep_aspect_ratio=True)

pdf.set_font('helvetica', 'B', 40)
pdf.cell(40, 30, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.output('shirtificate.pdf')
