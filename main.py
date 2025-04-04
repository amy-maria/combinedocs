import sys
import PyPDF2

# read each PDF, create new combined PDF in a new document
inputs = sys.argv[1:]
print(inputs)


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write("super.pdf")


pdf_combiner(inputs)

# super.pdf is not corrupted when opening from the project folder with Reader
