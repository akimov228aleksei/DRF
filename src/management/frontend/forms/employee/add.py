from django import forms


class AddEmployeeForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100,
                                 widget=forms.TextInput(
                                     attrs={"class": "form-control form-control-lg",
                                            "placeholder": "First name"}))
    second_name = forms.CharField(label='Second name', max_length=150,
                                  widget=forms.TextInput(
                                      attrs={"class": "form-control form-control-lg",
                                             "placeholder": "Enter Second name"}))
    birthday = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'type': 'date'}))
    department = forms.ChoiceField(required=False, widget=forms.Select(
        attrs={'class': 'form-control form-control-lg'}))
    position = forms.ChoiceField(required=False, widget=forms.Select(
        attrs={'class': 'form-control form-control-lg'}))
    salary = forms.IntegerField(min_value=0, max_value=100000, widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg',
               "placeholder": "Enter salary"}))
    on_boarding_day = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'type': 'date'}))

    def __init__(self, data=None, department_list=None, position_list=None, *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        if department_list and position_list:
            self.fields['position'] = forms.ChoiceField(choices=position_list, widget=forms.Select(
                attrs={'class': 'form-control form-control-lg'}))
            self.fields['department'] = forms.ChoiceField(choices=department_list, widget=forms.Select(
                attrs={'class': 'form-control form-control-lg'}))
