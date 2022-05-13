from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from datetime import datetime


class DepartmentHome(View):
    """Class for rendering the home page of departments"""

    template_name = 'department/department.html'

    def get(self, request):
        r = requests.get('http://127.0.0.1:8000/api/v1/department/',
                         headers={'Authorization': f'Token {request.COOKIES.get("Token")}'})
        if status.is_success(r.status_code):
            return render(request, 'department.html', {'content': r.json()})
        return render(request, 'preview.html')
