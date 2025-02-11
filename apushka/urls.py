from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rent_house.urls")),
    path("imagefit/", include("imagefit.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
