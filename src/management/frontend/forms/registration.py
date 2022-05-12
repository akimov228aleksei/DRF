from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    email = forms.EmailField(widget=forms.EmailInput)
