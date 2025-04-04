import sys
import PyPDF2

# read each PDF, create new combined PDF in a new document
inputs = sys.argv[1:]

template = PyPDF2.PdfReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open("watermarked_output.pdf", "wb") as file:
        output.write(file)


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write("super.pdf")


pdf_combiner(inputs)

# super.pdf is not corrupted when opening from the project folder with Reader
