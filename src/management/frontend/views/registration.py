from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from ..forms.registration import RegistrationForm


class RegistrationView(View):
    """Class for registration"""

    template_name = 'registration.html'

    def get(self, request):
        form = RegistrationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            r = requests.post('http://127.0.0.1:8000/api/v1/auth/users/',
                              files={'username': (None, form.data['username']),
                                     'password': (None, form.data['password']),
                                     'email': (None, form.data['email'])})

            if status.is_success(r.status_code) or status.is_redirect(r.status_code):
                return redirect('home')
            return render(request, self.template_name, {'form': form, 'status': r.text})
        else:
            return render(request, self.template_name, {'form': form})
