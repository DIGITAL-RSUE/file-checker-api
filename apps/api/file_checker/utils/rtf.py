from striprtf.striprtf import rtf_to_text

from .error_messages import ErrorMessages


def validate_rtf(file_name, file_data, **kwargs):
    init_file = kwargs.pop("file_for_check")
    try:
        with init_file.open() as infile:
            content = infile.read().decode()
            rtf_to_text(content)
    except Exception:
        return [ErrorMessages.CORRUPTED_FILE]
