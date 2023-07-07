from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('user', views.user_list, name='user'),
]