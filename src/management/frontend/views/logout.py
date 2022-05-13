from django.http import HttpResponseNotFound
from rest_framework import status
from django.shortcuts import redirect
from django.views.generic import View
import requests


class LogoutView(View):
    """Class for logout"""

    def post(self, request):
        r = requests.post('http://127.0.0.1:8000/api/v1/auth/token/logout/',
                          headers={'Authorization': f'Token {request.COOKIES.get("Token")}'})

        if status.is_success(r.status_code):
            # If token is deleted, then it is added to the cookies
            response = redirect('home')
            response.set_cookie('Token', '')
            return response
        return HttpResponseNotFound()
