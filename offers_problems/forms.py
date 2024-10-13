from django import forms
from offers_problems.models import ProblemModel, OfferModel


class ProblemModelForm(forms.ModelForm):
    class Meta:
        model = ProblemModel
        fields = '__all__'


class OfferForm(forms.Form):
    title = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)
