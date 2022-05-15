from django import forms
from service_objects.services import Service

from ..utils import (
    check_macro_in_ole_files,
    find_js_in_pdf,
    get_file_extension,
    validate_ole,
    validate_pdf,
    validate_rtf,
)


class CheckVulnerabilities(Service):
    """ Сервис для проверки файлов на уязвимость"""

    extensions_tests_mapping = {
        (validate_rtf,): ["rtf"],
        (validate_pdf, find_js_in_pdf): ["pdf"],
        (validate_ole, check_macro_in_ole_files): [
            "xls",
            "xlm",
            "xlsx",
            "xlsm",
            "doc",
            "docx",
            "docm",
            "ppt",
            "pps",
            "pptx",
            "ppsx",
            "ppam",
            "odt",
            "odp",
            "ods",
            "pptm",
        ],
    }

    file_for_check = forms.Field()

    def process(self):
        file_for_check = self.cleaned_data["file_for_check"]
        result = self.run_test(file_for_check)
        return result

    def compare_test(self, file_extension):
        test_list = []
        for tests, extensions in self.extensions_tests_mapping.items():
            if file_extension in extensions:
                for test in tests:
                    test_list.append(test)
        return test_list

    def run_test(self, file_for_check):
        file_name = file_for_check.name
        file_data = file_for_check.read()
        file_extension = get_file_extension(file_name)
        test_list = self.compare_test(file_extension)
        messages = []
        for test in test_list:
            results = test(file_name, file_data, file_for_check=file_for_check)
            if results:
                for result in results:
                    messages.append(result)

        return list(set(messages))
