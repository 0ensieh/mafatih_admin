from django.urls import path, include

urlpatterns = [
    path("", include("prayer.admin.views.urls"))
]
