from django.urls import path
from . import *

urlpatterns = [
    path("", categories, name='admin_categories'),
    path("create/", category_create, name='admin_category_create'),
    path("<int:id>/", category_edit, name='admin_category_edit'),

    path("full-hierarchy/", category_full_hierarchy, name='admin_category_full_hierarchy')
]
