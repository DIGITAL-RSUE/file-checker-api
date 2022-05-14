from io import BytesIO

from pdfid import pdfid
from PyPDF2 import PdfFileReader

from .error_messages import ErrorMessages


def validate_pdf(file_name, data ,**kwargs):
    try:
        PdfFileReader(BytesIO(data))
    except Exception:
        return [ErrorMessages.COMBINED_FILE, ErrorMessages.CORRUPTED_FILE]


def find_js_in_pdf(file_name, data ,**kwargs):
    options = pdfid.get_fake_options()
    options.scan = True
    options.json = True
    result = pdfid.PDFiDMain([file_name], options, [data])
    print(result)
    if (
        result["reports"][0]["/JavaScript"] > 0
        or result["reports"][0]["/JS"] > 0
    ):
        return [ErrorMessages.HAS_JS]
