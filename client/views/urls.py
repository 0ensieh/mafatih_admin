from django.urls import path
from . import *

urlpatterns = [
    path("login/", login, name='login'),
    path("logout/", logout, name='logout'),
    # path("login_sms/", login_sms, name='login_sms'),
    # path("verification_code/<str:cellphone>/", verification_code, name='verification_code'),
    # path("profile/", profile, name='profile'),
]
