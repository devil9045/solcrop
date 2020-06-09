import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import glob

name_pdf = glob.glob("*.pdf")
num_pdf = len(name_pdf)
for num in range(num_pdf):

    name = name_pdf[num]
    reader = PdfFileReader(f'{name}', 'r')
    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        page.cropBox.setLowerLeft((100, 10))
        page.cropBox.setLowerRight((750, 10))
        page.cropBox.setUpperLeft((100, 450))
        page.cropBox.setUpperRight((750, 450))
        writer.addPage(page)

    outstream = open(f'00({name})', 'wb')
    writer.write(outstream)
    outstream.close()




