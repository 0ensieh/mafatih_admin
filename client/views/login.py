from .imports import *


@csrf_exempt
def login(request):
    if request.method == "POST":
        cellphone = request.POST.get('cellphone')
        password = request.POST.get('password')
        
        try:
            user = User.get_user(cellphone)

            if user is None:
                messages.add_message(request, messages.ERROR, "نام کاربری وجود ندارد")
                return render(request, f'{__name__.replace(".", "/")}.html')
            # user = User.objects.get(Q(cellphone=cellphone) | Q(email=cellphone))
        except (User.DoesNotExist, Exception) as e:
            # cellphone is not exists
            print(str(e))
            messages.add_message(request, messages.ERROR, "نام کاربری وجود ندارد")
            return render(request, f'{__name__.replace(".", "/")}.html')
        
        user = authenticate(username=user.username, password=password)
        if user is not None:
            # user login successfully
            django_login(request, user)
            return redirect(reverse('dashboard'))
        messages.add_message(request, messages.ERROR, "یوزرنیم یا پسورد درست نیست")
    return render(request, f'{__name__.replace(".", "/")}.html')
