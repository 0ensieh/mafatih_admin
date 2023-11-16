from .imports import *


# @csrf_exempt
def signup(request):
    if request.method == 'POST':
        if not User.user_exists(request.POST.get('cellphone'), request.POST.get('email')):
            # check the email, cellphone and password existing
            try:
                _ = request.POST['cellphone']
            except (Exception, KeyError) as exception:
                print(exception)
                messages.add_message(request, messages.ERROR, "لطفا شماره تلفن را وارد کنید")
                return render(request, f'{__name__.replace(".", "/")}.html')
            
            # creating new user
            user = User()
            user.cellphone = request.POST.get('cellphone')
            user.username = request.POST.get('cellphone')
            # user.email = request.POST.get('email')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.set_password(request.POST.get('password'))
            user.save()
            return redirect(reverse("client:verification_code", kwargs={'cellphone': user.cellphone}))
        else:
            # user is already exists
            messages.add_message(request, messages.ERROR, "شماره تماس یا ایمیل، قبلا ثبت شده است")
    return render(request, f'{__name__.replace(".", "/")}.html')
