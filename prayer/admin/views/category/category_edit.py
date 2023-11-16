from .imports import *


# @login_required
def category_edit(request, id):
    context = {}
    c = None
    selected_prayers = None

    # GET CATEGORY
    try:
        c = Category.objects.prefetch_related(
            Prefetch(
                lookup="prayer",
                queryset=Prayer.objects.filter(category=id),
            )
        ).get(id=id, deleted=False)
        selected_prayers = list(c.prayer.values_list("id", flat=True))
    except (Category.DoesNotExist, Exception) as e:
        print(str(e))
        return redirect(reverse("prayer:admin_categories"))
    # END GET CATEGORY

    context['category'] = c
    context['prayers'] = Prayer.objects.filter()
    context['selected_prayers'] = selected_prayers

    # DELETE CATEGORY #
    if bool(request.GET.get("deleted", "")):
        c.deleted = True
        prayers = Prayer.objects.filter(id__in=selected_prayers)
        for p in prayers:
            c.prayer.remove(p)

        children = c.get_children()
        if c.parent:
            for item in children:
                item.parent = c.parent
                item.save()
        elif c.parent is None:
            for item in children:
                item.parent = None
        c.parent_id = None

        # SAVE TREE
        try:
            c.save()
        except Exception as e:
            print(str(e))
            c._tree_manager.rebuild()
            c.save()
        # END SAVE TREE

        return redirect(reverse("prayer:admin_categories"))
    # END DELETE CATEGORY #

    if request.method == "POST":
        # CHECK DUPLICATE
        if Category.objects.filter(deleted=False, title=request.POST.get("title", "").strip()).exclude(id=id).exists():
            messages.add_message(request, messages.ERROR, "مورد از قبل ساخته شده")
            return render(request, f'{__name__.replace(".", "/")}.html', context)
        # END CHECK DUPLICATE

        c.title = request.POST.get("title", "").strip()
        c.publish = bool(int(request.POST.get("publish", "1").strip()))
        c.index = bool(int(request.POST.get("index", "1").strip()))
        if request.POST.get("parent", ""):
            try:
                c.parent = Category.objects.get(id=int(request.POST.get("parent", "")))
            except (Category.DoesNotExist, Exception) as e:
                print(str(e))
        else:
            c.parent = None

        # SAVE TREE
        try:
            c.save()
        except Exception as e:
            print(str(e))
            c._tree_manager.rebuild()
            c.save()
        # END SAVE TREE

        # SET PRAYERS
        sel = list(map(lambda item: int(item), request.POST.getlist("prayer_ids", "")))
        add = []
        delete = []
        for item in sel:
            if item not in selected_prayers:
                add.append(item)
        for item in selected_prayers:
            if item not in sel:
                delete.append(item)

        for item in delete:
            c.prayer.remove(Prayer.objects.get(id=item))
        for item in add:
            c.prayer.add(Prayer.objects.get(id=item))
        context['selected_prayers'] = c.prayer.all().values_list("id", flat=True)
        # END SET PRAYERS

        messages.add_message(request, messages.SUCCESS, "بروزرسانی شد")

    non_parents = list(c.get_descendants().values_list("id", flat=True))
    non_parents.append(c.id)
    context['parents'] = Category.objects.filter(deleted=False).exclude(id__in=non_parents)
    return render(request, f'{__name__.replace(".", "/")}.html', context)
