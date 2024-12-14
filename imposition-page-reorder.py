import PyPDF2

# use a virtual environment 
#    python -m venv .venv 
# install pyPDF2 via pip

def rearrange_pdf(input_pdf, output_pdf):
    # Open the input PDF file
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)

        if num_pages % 2 != 0:
            raise ValueError("The PDF must have an even number of pages for proper booklet arrangement.")

        # Calculate the new order for printer spreads
        new_order = []
        left = 0
        right = num_pages - 1

        while left < right:
            new_order.append(left)   # Add the left-side page
            new_order.append(right)  # Add the right-side page
            left += 1
            right -= 1

        # Create a new PDF writer object
        writer = PyPDF2.PdfWriter()

        # Add pages to the writer in the new order
        for page_index in new_order:
            writer.add_page(reader.pages[page_index])

        # Write the new PDF file
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

    print(f"Reordered PDF saved as: {output_pdf}")


# Example usage
input_pdf = "input.pdf"  # Replace with the path to your input PDF
output_pdf = "output_printer_ready.pdf"  # Replace with the desired output file name

rearrange_pdf(input_pdf, output_pdf)
