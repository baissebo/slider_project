from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from slider.views import SliderView

urlpatterns = [
    path("", SliderView.as_view(), name="slider"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
