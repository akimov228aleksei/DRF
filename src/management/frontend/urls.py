"""Module with Frontend URL ratios"""

from django.urls import path, include
from frontend.views import department, authorization, registration, logout


urlpatterns = [
    path('', department.DepartmentHome.as_view(), name='home'),
    path('authorization/', authorization.AuthorizationView.as_view(), name='authorization'),
    path('registration/', registration.RegistrationView.as_view(), name='authorization'),
    path('logout/', logout.LogoutView.as_view(), name='logout'),
]
