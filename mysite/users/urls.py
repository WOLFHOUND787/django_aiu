from os import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.users, name='users'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)