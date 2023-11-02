from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Test PDF Document', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

text = """
The Physics of Gymnastics

Gymnastics is not only a sport that demonstrates incredible flexibility and strength but is also a demonstration of the laws of physics. The balance beam, rings, vault, and floor exercises are all performances that can be analyzed through the lens of physics.

Gravity, momentum, force, and velocity are all key elements that a gymnast must harness to perform a routine. Understanding the underlying physics can enhance a gymnast's performance and increase their score in competitions.

This PDF is created for testing a command-line program that converts PDF text into audio format.
"""

pdf.multi_cell(0, 10, text)
pdf.output('test_document.pdf')
