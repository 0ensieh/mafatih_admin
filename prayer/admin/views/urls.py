from django.urls import path, include
from . import *

urlpatterns = [
    path("prayers/", prayers, name="admin_prayers"),
    path("prayer/create/", prayer_create, name="admin_prayer_create"),
    path("prayer/<int:id>/", prayer_edit, name="admin_prayer_edit"),
    path("prayers/full-hierarchy/", prayer_full_hierarchy, name="admin_prayer_full_hierarchy"),
    path("prayer/<int:prayer_id>/phrases/", include("prayer.admin.views.phrase.urls")),

    path("category/", include("prayer.admin.views.category.urls"))
]
