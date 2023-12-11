from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    initial_text = _('')
    input_text = _('')
    clear_checkbox_label = _('Remover')

