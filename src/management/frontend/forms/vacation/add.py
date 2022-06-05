from django import forms
from django.core.exceptions import ValidationError


class AddVacationForm(forms.Form):
    employee = forms.ChoiceField(required=False, widget=forms.Select(
        attrs={'class': 'form-control form-control-lg'}))
    start_date = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'type': 'date'}))

    def __init__(self, data=None, employee_list=None, *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        if employee_list:
            self.fields['employee'] = forms.ChoiceField(choices=employee_list, widget=forms.Select(
                attrs={'class': 'form-control form-control-lg'}))

    def clean_end_date(self):
        """The method which checking date"""

        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        # Raise error if start date is later than end date
        if start_date >= end_date:
            raise ValidationError("End date cannot be earlier than start date")
