from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Set font
        self.set_font('arial', 'B', 20)
        # Move cursor to the right:
        self.cell(80)

        # Print title
        self.cell(30, 10, 'CS50 Shirtificate', border=1, align='C')
        # perform a line break:
        self.ln(20)



pdf = FPDF()
pdf.add_page()
# pdf.set_font('arial', 'B', 18)
# pdf.cell(40, 10, 'Abc')
pdf.output('shirtificate.pdf')
