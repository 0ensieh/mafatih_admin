from .imports import *


def logout(request):
    django_logout(request)
    return redirect(reverse("dashboard"))
