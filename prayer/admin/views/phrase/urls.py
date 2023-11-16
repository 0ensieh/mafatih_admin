from django.urls import path
from . import *

urlpatterns = [
    # path("", phrases, name='admin_phrases'),
    path("create/", phrase_create, name='admin_phrase_create'),
    path("<str:order>/", phrase_edit, name='admin_phrase_edit'),
]
