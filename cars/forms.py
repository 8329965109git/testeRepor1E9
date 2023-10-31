# Import the necessary classes and modules from Django
from django import forms

# Import the 'Maker' model from your application's models module
from .models import Maker

# Create a ModelForm for the 'Maker' model


class MakerForm(forms.ModelForm):
    class Meta:
        # Specify the model to use for the form
        model = Maker
        # Include all fields from the 'Maker' model in the form
        fields = "__all__"
