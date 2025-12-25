from src.ocr import extract_text_from_pdf
from src.extract_fields import extract_invoice_fields
from src.validate import validate_invoice
from src.load_db import load_to_db

pdf_path = "data/raw/sample_invoice.pdf"

text = extract_text_from_pdf(pdf_path)
invoice_data = extract_invoice_fields(text)

if validate_invoice(invoice_data):
    load_to_db(invoice_data)
    print("Invoice processed successfully")
else:
    print("Validation failed")