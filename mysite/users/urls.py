from django.urls import path
from users.views import register, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
]
