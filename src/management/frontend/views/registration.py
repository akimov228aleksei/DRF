from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from ..forms.registration import RegistrationForm
from frontend.views import authorization


class RegistrationView(View):
    """Class for registration"""

    template_name = 'registration.html'

    def get(self, request):
        # If user is authorized, then redirect on 'home'
        if request.COOKIES.get('Token'):
            return redirect('home')
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
                # If user is created, he is automatically authorized
                auth = authorization.AuthorizationView()
                return auth.post(request)
            return render(request, self.template_name, {'form': form, 'status': r.text})
        else:
            return render(request, self.template_name, {'form': form})
