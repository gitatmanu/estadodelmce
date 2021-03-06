from django.contrib import admin
from django.urls import path
from estadodelmce import settings
from django.conf.urls.static import static

from estadodelmce.views import IndexView, CommunistPartiesView

urlpatterns = [
    path('', IndexView.as_view()),
    path('lista-de-partidos/', CommunistPartiesView.as_view(), name="communistparty_list"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
