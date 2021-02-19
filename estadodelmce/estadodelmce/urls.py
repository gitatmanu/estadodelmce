from django.contrib import admin
from django.urls import path
from estadodelmce import settings
from django.conf.urls.static import static

from estadodelmce.views import CommunistPartyView

urlpatterns = [
    path('', CommunistPartyView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)