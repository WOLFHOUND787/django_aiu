from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('about/', blog_views.about, name='about'),
    path('users/', include('users.urls')),
]
