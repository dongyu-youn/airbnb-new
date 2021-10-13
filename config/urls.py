from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include


urlpatterns = [
   path("admin/", admin.site.urls),
   path("rooms/", include("core.urls")),
#    o 일단 모든 데이터를 출력시켜보자

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
