from django.forms import Field, Form, ValidationError


def get_forms_class(*, fields: dict):
    """
    Функция которая генерирует класс формы с указанными полями.

    Args:
        fields (dict): Поля формы

    Returns:
        [Form]: Класс формы
    """
    return type("", (Form,), fields)


class FormField(Field):
    """
    A field for class `Service` that accepts a list of objects which is
    translated into multiple class `Form`

    ```
        class PersonForm(forms.Form):
            name = forms.CharField()


        class UpdateOrganizationService(Service):
            person = FormField(PersonForm)

            def process(self):
                person = self.cleaned_data['person']
                print(person.cleaned_data['name'])

        UpdateOrganizationService.execute({
            'person': { 'name': 'John Smith' }
        })
    ```
    """

    def __init__(self, form_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = form_class

    def clean(self, value):
        form = self.form_class(value)

        if not form.is_valid():
            raise ValidationError(repr(form.errors))

        return form
