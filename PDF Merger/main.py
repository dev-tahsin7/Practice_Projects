from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ['p1.pdf', 'p2.pdf']:
    merger.append(pdf)

merger.write('merged-pdf.pdf')
merger.close()