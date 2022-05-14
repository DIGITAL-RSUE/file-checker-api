from .error_messages import ErrorMessages


def get_file_extension(file_name):
    try:
        return file_name[file_name.rfind(".") + 1 :]
    except Exception:
        return [ErrorMessages.COMBINED_FILE, ErrorMessages.CORRUPTED_FILE]
