from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

# This script will create a document of one landscape a4 from two portrait a5 to create a a5 booklet
# with pages 12-1, 2-11, 3-10, 4-9, 5-8, 6-7 to allow printing

# use a venv
# pip install pyPDF2 reportlab PyCryptodome

def merge_pages(input_pdf, output_pdf, page_order):
    # Load the input PDF
    reader = PdfReader(input_pdf)
    num_pages = len(reader.pages)
    
    if len(page_order) * 2 != num_pages:
        raise ValueError("Page order doesn't match the number of pages in the PDF.")

    # Prepare the PDF writer
    writer = PdfWriter()

    for left_page, right_page in page_order:
        # Create a new blank A4 landscape page
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=A4)

        # Add left page (portrait, placed on the left of the A4 landscape)
        if left_page > 0:  # Ignore if the page is invalid
            left_page_index = left_page - 1
            left_page_content = reader.pages[left_page_index]
            c.drawInlineImage(io.BytesIO(left_page_content.extract_text()), 0, 0)
