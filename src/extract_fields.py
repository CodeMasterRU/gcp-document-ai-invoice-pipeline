import re

def extract_invoice_fields(text):
    return {
        "invoice_number": extract(r"Invoice\s*No[:\s]+(\S+)", text),
        "invoice_date": extract(r"Date[:\s]+([\d/.-]+)", text),
        "supplier": extract(r"Supplier[:\s]+(.+)", text),
        "total_amount": extract(r"Total[:\s]+([\d,.]+)", text),
        "currency": "EUR",
        "vat": extract(r"VAT[:\s]+([\d,.]+)", text)
    }

def extract(pattern, text):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None