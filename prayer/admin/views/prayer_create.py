from .imports import *


# @login_required
def prayer_create(request):
    context = {}
    if request.method == 'POST':
        if Prayer.objects.filter(name=request.POST.get("name", "").strip()).exists():
            messages.add_message(request, messages.ERROR, "مورد از قبل ساخته شده")
            # context['prayers'] = Prayer.objects.filter()
            return render(request, f'{__name__.replace(".", "/")}.html', request.POST)
        with transaction.atomic():
            p = Prayer()
            p.name = request.POST.get("name", "").strip()
            p.publish = bool(int(request.POST.get("publish", "")))
            if request.POST.get("parent", ""):
                try:
                    p.parent = Prayer.objects.get(id=int(request.POST.get("parent", "")))
                except (Prayer.DoesNotExist, Exception) as e:
                    print(str(e))
            p.save()

            # ADD LINK PRAYERS
            links: list[int] = list(map(lambda item: int(item), request.POST.getlist("link", "")))
            p.update_links(links)
            p.save()
            # END ADD LINK PRAYERS

            # ADD PHRASES
            if request.POST.get("phrases", ""):
                phrases: list[str] = request.POST.get("phrases", "").split("\n")
                phrases = list(filter(lambda i: not i.isspace(), phrases))
                phrases_list: list[Phrase] = []
                order = 1
                for item in phrases:
                    phrase = Phrase()
                    item = item.replace("\r", "")
                    if item.startswith("#") and item.endswith("#"):
                        phrase.type = 2
                        item = item.replace("#", "")
                    elif item.startswith("$") and item.endswith("$"):
                        phrase.type = 3
                        item = item.replace("$", "")
                    else:
                        phrase.type = 1
                    phrase.text = item
                    phrase.prayer_id = p.id
                    phrase.order = f'{p.id}_{order}'

                    phrases_list.append(phrase)
                    order += 1
                if len(phrases_list) != 0:
                    Phrase.objects.bulk_create(phrases_list, len(phrases_list))
            # END ADD PHRASES
        return redirect(reverse("prayer:admin_prayer_edit", kwargs={"id": p.id}))
    context['prayers'] = Prayer.objects.filter()
    return render(request, f'{__name__.replace(".", "/")}.html', context)
