from django import forms


class AuthorizationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={"class": "form-control form-control-lg",
                                                             "placeholder": "Enter username"}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg",
                                                                 "placeholder": "Enter password"}))
