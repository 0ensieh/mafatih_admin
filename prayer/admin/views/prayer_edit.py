from .imports import *


# @login_required
def prayer_edit(request, id):
    context = {}
    p = None
    try:
        p = Prayer.objects.prefetch_related(
            Prefetch(
                lookup="phrase_set",
                queryset=Phrase.objects.filter(prayer_id=id, deleted=False),
            )
        ).get(id=id)
    except (Category.DoesNotExist, Exception) as e:
        print(str(e))
    if request.method == 'POST':
        if Prayer.objects.filter(name=request.POST.get("name", "").strip()).exclude(id=id).exists():
            messages.add_message(request, messages.ERROR, "مورد از قبل ساخته شده")
            context['prayer'] = p
            true_parents = p.get_ancestors().values_list('id', flat=True)
            non_parents = p.get_family().exclude(id__in=true_parents).values_list('id', flat=True)
            context['parents'] = Prayer.objects.exclude(id__in=non_parents)
            return render(request, f'{__name__.replace(".", "/")}.html', context)

        p.name = request.POST.get("name", "")
        p.publish = bool(int(request.POST.get("publish", "")))
        if request.POST.get("parent", ""):
            try:
                p.parent = Prayer.objects.get(id=int(request.POST.get("parent", "")))
            except (Prayer.DoesNotExist, Exception) as e:
                print(str(e))
        else:
            p.parent = None
        p.save()

        # ADD LINK PRAYERS
        links: list[int] = list(map(lambda item: int(item), request.POST.getlist("link", "")))
        p.update_links(links)
        p.save()
        # END ADD LINK PRAYERS

        messages.add_message(request, messages.SUCCESS, "بروزرسانی شد")
    context['prayer'] = p
    true_parents = p.get_ancestors().values_list('id', flat=True)
    non_parents = p.get_family().exclude(id__in=true_parents).values_list('id', flat=True)
    context['parents'] = Prayer.objects.exclude(id__in=non_parents)
    context['prayers'] = Prayer.objects.filter()
    return render(request, f'{__name__.replace(".", "/")}.html', context)
