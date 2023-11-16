from .imports import *


# @login_required
def categories(request):
    context = {}
    context['categories'] = Category.objects.filter(deleted=False)
    return render(request, f'{__name__.replace(".", "/")}.html', context)
