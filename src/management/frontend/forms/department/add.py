from django import forms


class AddDepartmentForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100,
                            widget=forms.TextInput(attrs={"class": "form-control form-control-lg",
                                                          "placeholder": "Enter title"}))
    description = forms.CharField(label='Description', max_length=150,
                                  widget=forms.TextInput(attrs={"class": "form-control form-control-lg",
                                                                "placeholder": "Enter Description"}))
