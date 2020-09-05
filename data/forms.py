from django.forms import ModelForm

from data.models import Data


class DataForm(ModelForm):
    """Form for adding data."""
    class Meta:
        model = Data
        exclude = ["identifier"]