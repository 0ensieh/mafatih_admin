from .imports import *


# @login_required
def category_create(request):
    context = {}
    context['prayers'] = Prayer.objects.filter()
    context['categories'] = Category.objects.filter()
    if request.method == 'POST':
        if Category.objects.filter(title=request.POST.get("title", "").strip()).exists():
            messages.add_message(request, messages.ERROR, "مورد از قبل ساخته شده")
            context['title'] = request.POST.get("title", "").strip()
            context['parent'] = int(request.POST.get("parent", "").strip())
            context['prayer_ids'] = list(map(lambda item: int(item), request.POST.getlist("prayer_ids", "")))
            return render(request, f'{__name__.replace(".", "/")}.html', context)
        c = Category()
        c.title = request.POST.get("title", "").strip()
        c.publish = bool(int(request.POST.get("publish", "1").strip()))
        c.index = bool(int(request.POST.get("index", "1").strip()))
        if request.POST.get("parent", ""):
            try:
                c.parent = Category.objects.get(id=int(request.POST.get("parent", "").strip()))
            except (Category.DoesNotExist, Exception) as e:
                print(str(e))
        c.save()

        if request.POST.getlist("prayer_ids", ""):
            prayer_ids = list(map(lambda item: int(item), request.POST.getlist("prayer_ids", "")))
            prayers = Prayer.objects.filter(id__in=prayer_ids)
            for p in prayers:
                c.prayer.add(p)

        messages.add_message(request, messages.SUCCESS, "دسته‌بندی ساخته شد")
        return redirect(reverse("prayer:admin_category_edit", kwargs={"id": c.id}))
    return render(request, f'{__name__.replace(".", "/")}.html', context)
