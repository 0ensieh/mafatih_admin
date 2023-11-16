from .imports import *


# @login_required
def phrase_create(request, prayer_id):
    context = {}
    try:
        prayer = Prayer.objects.prefetch_related(
            Prefetch(
                "phrase_set",
                queryset=Phrase.objects.filter(prayer_id=prayer_id)
            )
        ).get(id=prayer_id)
    except (Prayer.DoesNotExist, Exception) as e:
        print(str(e))
        return redirect(reverse("prayer:admin_prayers"))
    if request.method == 'POST':
        if Phrase.objects.filter(text=request.POST.get("text", "").strip()).exists():
            messages.add_message(request, messages.ERROR, "فراز از قبل ساخته شده")
            context['prayer'] = prayer
            context['text'] = request.POST.get("text", "").strip()
            return render(request, f'{__name__.replace(".", "/")}.html', context)
        phrase = Phrase()
        phrase.text = request.POST.get("text", "").strip()
        phrase.type = int(request.POST.get("type", "").strip())
        print(prayer.phrase_set)
        last_phrase = int(prayer.phrase_set.order_by("-order").first().order.split("_")[-1]) + 1
        phrase.order = f"{prayer_id}_{last_phrase}"
        phrase.prayer_id = prayer_id
        phrase.save()
        messages.add_message(request, messages.ERROR, "فراز با موفقیت ساخته شد")
        return redirect(reverse("prayer:admin_prayer_edit", kwargs={"id": prayer_id}))
    context['prayer'] = prayer
    return render(request, f'{__name__.replace(".", "/")}.html', context)
