from .imports import *


# @login_required
def category_full_hierarchy(request):
    context = {}
    context['full_hierarchy'] = Category.get_full_hierarchy()
    return render(request, f'{__name__.replace(".", "/")}.html', context)
