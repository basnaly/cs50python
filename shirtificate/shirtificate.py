from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font('arial', 'B', 18)
pdf.cell(40, 10, 'Abc')
