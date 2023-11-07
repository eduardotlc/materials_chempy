def extract_text_from_pdf(pdf_path):
    """ Returns a string containing all pdf readable words. It no argument is given, pdf_path
    fallback to default pdf example file.

    :param pdf_path: Path to pdf file, defaults to './test.pdf'
    :type pdf_path: str, optional
    :return: A string conataining every readable word of the PDF
    :rtype: str

    """
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text


def is_numeric(word):
    try:
        float(word)
        return True
    except ValueError:
        return False