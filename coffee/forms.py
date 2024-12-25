from django import forms
from .models import CoffeeQuality
from crispy_forms.helper import FormHelper

class CoffeeQualityForm(forms.ModelForm):

    class Meta:
        model = CoffeeQuality
        exclude = ('species', 'variety', 'year', 'colour', 'processing_method', 'country', 'uniformity', 'sweetness', 'moisture',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'),]
        self.fields['aroma'] = forms.ChoiceField(choices=categories)
        self.fields['flavour'] = forms.ChoiceField(choices=categories)
        self.fields['aftertaste'] = forms.ChoiceField(choices=categories)
        self.fields['acidity'] = forms.ChoiceField(choices=categories)
        self.fields['body'] = forms.ChoiceField(choices=categories)
        self.fields['balance'] = forms.ChoiceField(choices=categories)

        self.helper = FormHelper(self)
        self.helper.field_class = 'mb-3'
        self.helper.label_class = 'form-label'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-select'
