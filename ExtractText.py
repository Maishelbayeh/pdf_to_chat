import pdfplumber

def ExtractText(pdf_path):
    extracted_text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through each page of the PDF
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"  # Append text with a newline
    
    return extracted_text

# Example usage
