from .imports import *


# @login_required
def prayers(request):
    context = {}
    context['prayers'] = Prayer.objects.all()
    return render(request, f'{__name__.replace(".", "/")}.html', context)
