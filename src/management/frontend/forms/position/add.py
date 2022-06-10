from django import forms


class AddPositionForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100,
                            widget=forms.TextInput(attrs={"class": "form-control form-control-lg",
                                                          "placeholder": "Enter position name"}))
    max_salary = forms.IntegerField(label='Max salary', min_value=0, max_value=100000,
                                    widget=forms.NumberInput(attrs={"class": "form-control form-control-lg",
                                                                    "placeholder": "Enter max salary"}))
