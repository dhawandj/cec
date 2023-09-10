# 10. AIM: Demonstration of working with PDF, word and JSON files
# a) Write a python program to combine select pages from many PDFsfrom PyPDF2 import
# PdfWriter, PdfReader
# Code:
from PyPDF2 import PdfWriter, PdfReader


def combine_pages(selected_pages, output_file):
    pdf_writer = PdfWriter()

    for pdf_file, page_numbers in selected_pages:
        pdf_reader = PdfReader(open(pdf_file, "rb"))
        for page_num in page_numbers:
            if 1 <= page_num <= len(pdf_reader.pages):
                page = pdf_reader.pages[page_num-1]
                pdf_writer.add_page(page)
            else:
                print(f"Page {page_num} is out of range for {pdf_file}.")

    with open(output_file, "wb") as output:
        pdf_writer.write(output)


# List of tuples containing PDF filenames and corresponding page numbers
selected_pages = [
    (
        "/Users/dhawanj/Desktop/engg_cutoff_gen_mock.pdf",
        [1, 2],
    ),  # Select page 1 and 2 from file1.pdf
    (
        
        "/Users/dhawanj/Desktop/engg_cutoff_gen_mock.pdf",
        [1, 2],
    ),  # Select page 2 and 4 from file2.pdf
    # Add more PDFs and page numbers as needed
]
output_filename = "combined_output.pdf"
combine_pages(selected_pages, output_filename)
