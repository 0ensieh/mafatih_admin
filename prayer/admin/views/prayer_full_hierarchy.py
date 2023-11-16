from .imports import *


# @login_required
def prayer_full_hierarchy(request):
    context = {}
    context['full_hierarchy'] = Prayer.get_full_hierarchy()
    return render(request, f'{__name__.replace(".", "/")}.html', context)
