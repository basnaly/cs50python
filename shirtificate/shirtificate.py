from fpdf import FPDF


class PDF(FPDF):

    def load_image('shirtificate.png'):
        # Render image:
        if isinstance('shirtificate.png', BytesIO):
            return 'shirtificate.png'

    def header(self):
        # Set font
        self.set_font('arial', 'B', 32)
        # Move cursor to the right:
        self.cell(80)
        # Set text color
        self.set_text_color(0, 0, 0)

        # Print header
        self.cell(30, 10, 'CS50 Shirtificate', border=1, align='C')
        # perform a line break:
        self.ln(20)

    def title(self):
        # Set font
        self.set_font('arial', 'B', 16)
        # Move cursor to the right:
        self.cell(80)
        # Set text color
        self.set_text_color(255, 255, 255)

        # Print title
        self.cell(30, 10, 'John Harvard took CS50', border=1, align='C')
        # perform a line break:
        self.ln(20)


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
# pdf.set_font('arial', 'B', 18)
# pdf.cell(40, 10, 'Abc')
pdf.output('shirtificate.pdf')
