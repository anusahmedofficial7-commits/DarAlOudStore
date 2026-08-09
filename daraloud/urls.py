from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # =====================================
    # ADMIN
    # =====================================

    path(
        "admin/",
        admin.site.urls,
    ),


    # =====================================
    # STORE APP
    # =====================================

    path(
        "",
        include("store.urls"),
    ),

]


# =========================================
# MEDIA FILES - DEVELOPMENT
# =========================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )