import sys
try:
    from pypdf import PdfReader
    reader = PdfReader("/Users/rinouo/Frontend/Projects/Riin_Resume/林霈文104.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    print(text)
except ImportError:
    try:
        import pdfplumber
        with pdfplumber.open("/Users/rinouo/Frontend/Projects/Riin_Resume/林霈文104.pdf") as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            print(text)
    except ImportError:
        print("Error: Neither pypdf nor pdfplumber is installed.")
