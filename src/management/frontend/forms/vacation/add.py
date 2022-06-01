from django import forms


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
