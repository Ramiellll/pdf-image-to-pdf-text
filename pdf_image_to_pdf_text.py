import argparse
import cv2
import pytesseract
from pdf2image import convert_from_path
from fpdf import FPDF
# img = cv2.imread('image.png')

parser = argparse.ArgumentParser(
    prog="pdf_image_to_pdf_text", description="Convert pdf made with images in a normal pdf")

parser.add_argument('--input', '-i', action='store', required=True, help='File you want to convert')
parser.add_argument('--output', '-o', action='store', type=str, default="result", help='Name of the result')
args = parser.parse_args()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=13)

pages = convert_from_path(args.input, fmt="jpeg")

for page in pages:
    page.save('output.jpg', 'JPEG')
    img = cv2.imread('output.jpg')
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config).encode(
        'latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(300, 10, txt=text)

pdf.output(args.output + ".pdf")
