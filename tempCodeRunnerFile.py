import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import base64


def create_blank_page(output_buffer, message):
    c = canvas.Canvas(output_buffer, pagesize=letter)
    c.setFillColorRGB(0, 1, 1)
    encrypted_message = base64.b64encode(message.encode()).decode()
    c.drawString(100, 100, encrypted_message)
    c.drawString
    c.showPage()
    c.save()

def create_blank_page_with_image(image_path, output_buffer):
    c = canvas.Canvas(output_buffer, pagesize=letter)
    c.drawImage(image_path, 0, 0, width=letter[0], height=letter[1])
    c.showPage()
    c.save()

def edit_pdf_metadata(input_pdf, output_pdf, new_metadata, message, first_page_image_path):
    # Create a buffer to hold the PDF content
    output_buffer = io.BytesIO()

    # Create a blank page with the first page image
    create_blank_page_with_image(first_page_image_path, output_buffer)
    output_buffer.seek(0)

    # Create a PdfWriter object
    pdf_writer = PdfWriter()

    # Add the blank page to the writer
    blank_page = PdfReader(output_buffer).pages[0]
    pdf_writer.add_page(blank_page)

    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as file:
        pdf_reader = PdfReader(file)

        # Copy pages from the input PDF to the output PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    # Create a buffer for the last page
    output_buffer = io.BytesIO()

    # Create a blank page with the last page image
    create_blank_page(output_buffer, message)
    output_buffer.seek(0)

    # Add the last blank page to the writer
    blank_page = PdfReader(output_buffer).pages[0]
    pdf_writer.add_page(blank_page)

    # Update metadata
    pdf_writer.add_metadata(new_metadata)

    # Write the updated metadata to the output PDF file
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

# Input parameters
input_pdf = 'output/jurnal.pdf'
output_pdf = 'output/jurnal_FD.pdf'
new_metadata = {'/Title': 'Sejarah Digital Forensik', '/Author': 'Tejo', '/Subject': 'New Subject'}
message = "Kelas Digital Forensik Telkom University Surabaya"
first_page_image_path = 'telusby.png'

# Call the function
edit_pdf_metadata(input_pdf, output_pdf, new_metadata, message, first_page_image_path)