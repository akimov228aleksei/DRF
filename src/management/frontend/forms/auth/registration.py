from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={"class": "form-control form-control-lg",
                                                             "placeholder": "Enter username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control form-control-lg",
                                                            "placeholder": "Enter email"}))
    password = forms.CharField(min_length=8,
                               widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg",
                                                                 "placeholder": "password"}))
