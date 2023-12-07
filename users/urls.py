from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_users, name='home'),
    path('user_detail/<int:user_id>/', views.detail_user, name='detail'),
]
