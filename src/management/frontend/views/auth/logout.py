from django.http import HttpResponseNotFound
from rest_framework import status
from django.shortcuts import redirect, render
from django.views.generic import View
import requests


class LogoutView(View):
    """Class for logout"""

    url_logout = 'http://127.0.0.1:8000/api/v1/auth/token/logout/'
    preview_template = 'auth/preview.html'

    def post(self, request):

        # Getting token from cookies
        token = request.COOKIES.get("Token")
        # If token is absent -> redirect to authorization
        if token:
            api_request = requests.post(self.url_logout,
                                        headers={'Authorization': f'Token {token}'})

            if status.is_success(api_request.status_code):
                # If the token is removed, then it is removed from the cookie
                response = redirect('home')
                response.set_cookie('Token', '')
                return response
            return HttpResponseNotFound()
        return render(request, self.preview_template)
