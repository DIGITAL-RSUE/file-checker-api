from .files_base import get_file_extension
from .ole import check_macro_in_ole_files, validate_ole
from .pdf import find_js_in_pdf, validate_pdf
from .rtf import validate_rtf

__all__ = (
    "validate_ole",
    "check_macro_in_ole_files",
    "validate_pdf",
    "find_js_in_pdf",
    "get_file_extension",
    "validate_rtf",
)
