from django.urls import path, include

app_name = "prayer"

urlpatterns = [
    # path(f'{app_name}/', include(f'{app_name}.views.urls')),
    # path(f'api/{app_name}/', include(f'{app_name}.api.urls')),
    path(f'admin/{app_name}/', include(f'{app_name}.admin.urls'))
]
