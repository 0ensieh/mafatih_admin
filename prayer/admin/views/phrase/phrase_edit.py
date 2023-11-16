from .imports import *


# @login_required
def phrase_edit(request, prayer_id, order):
    context = {}
    try:
        prayer = Prayer.objects.prefetch_related(
            Prefetch(
                lookup="phrase_set",
                queryset=Phrase.objects.filter(prayer_id=prayer_id, order=order),
                to_attr="phrases"
            )
        ).get(id=prayer_id)
        phrase = prayer.phrases[0]
    except (Prayer.DoesNotExist, Exception) as e:
        print(str(e))
        return redirect(reverse("prayer:admin_prayers"))
    if request.method == 'POST':
        if Phrase.objects.filter(text=request.POST.get("text", "").strip()).exclude(order=order).exists():
            messages.add_message(request, messages.ERROR, "فراز از قبل ساخته شده")
            context['prayer'] = prayer
            context['phrase'] = phrase
            return render(request, f'{__name__.replace(".", "/")}.html', context)
        phrase.text = request.POST.get("text", "").strip()
        phrase.type = int(request.POST.get("type", "").strip())
        phrase.save()
        messages.add_message(request, messages.ERROR, "فراز با موفقیت ویرایش شد")
    context['prayer'] = prayer
    context['phrase'] = phrase
    return render(request, f'{__name__.replace(".", "/")}.html', context)
