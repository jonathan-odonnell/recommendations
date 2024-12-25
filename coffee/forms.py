from django import forms
from .models import CoffeeQuality
from crispy_forms.helper import FormHelper

class CoffeeQualityForm(forms.ModelForm):

    class Meta:
        model = CoffeeQuality
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'),]
        species = CoffeeQuality.objects.exclude(species=None).distinct('species')
        countries = CoffeeQuality.objects.exclude(country=None).distinct('country')
        years = CoffeeQuality.objects.exclude(year=None).distinct('year')
        varieties = CoffeeQuality.objects.exclude(variety=None).distinct('variety')
        colours = CoffeeQuality.objects.exclude(colour=None).distinct('colour')
        processing_methods = CoffeeQuality.objects.exclude(processing_method=None).exclude(processing_method='Other').distinct('processing_method')
        self.fields['species'] = forms.ChoiceField(choices=[(i.id, i.species) for i in species])
        self.fields['country'] = forms.ChoiceField(choices=[(i.id, i.country) for i in countries])
        self.fields['year'] = forms.ChoiceField(choices=[(i.id, i.year) for i in years])
        self.fields['variety'] = forms.ChoiceField(choices=[(i.id, i.variety) for i in varieties])
        self.fields['colour'] = forms.ChoiceField(choices=[(i.id, i.colour) for i in colours])
        self.fields['processing_method'] = forms.ChoiceField(choices=[(i.id, i.processing_method) for i in processing_methods])
        self.fields['aroma'] = forms.ChoiceField(choices=categories)
        self.fields['flavour'] = forms.ChoiceField(choices=categories)
        self.fields['aftertaste'] = forms.ChoiceField(choices=categories)
        self.fields['acidity'] = forms.ChoiceField(choices=categories)
        self.fields['body'] = forms.ChoiceField(choices=categories)
        self.fields['balance'] = forms.ChoiceField(choices=categories)
        self.fields['uniformity'] = forms.ChoiceField(choices=categories)
        self.fields['sweetness'] = forms.ChoiceField(choices=categories)
        self.fields['moisture'] = forms.ChoiceField(choices=categories)

        self.helper = FormHelper(self)
        self.helper.field_class = 'mb-3'
        self.helper.label_class = 'form-label'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-select'
