from oletools import olevba
from oletools.mraptor import MacroRaptor

from .error_messages import ErrorMessages


def validate_ole(file_name, data, **kwargs):
    try:
        olevba.VBA_Parser(filename=file_name, data=data)
    except Exception:
        return [ErrorMessages.COMBINED_FILE, ErrorMessages.CORRUPTED_FILE]


def check_macro_in_ole_files(file_name, data, **kwargs):
    try:
        vba_parser = olevba.VBA_Parser(filename=file_name, data=data)
    except Exception:
        return [ErrorMessages.COMBINED_FILE, ErrorMessages.CORRUPTED_FILE]
    if vba_parser.detect_vba_macros():
        vba_code_all_modules = ""
        try:
            vba_code_all_modules = vba_parser.get_vba_code_all_modules()
        except Exception:
            return [ErrorMessages.CORRUPTED_FILE]
        mraptor = MacroRaptor(vba_code_all_modules)
        mraptor.scan()
        if mraptor.suspicious:
            return [ErrorMessages.HAS_VIRUS_MACRO]
        else:
            return [ErrorMessages.HAS_MACRO_BUT_OK]
