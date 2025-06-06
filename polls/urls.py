from django.urls import path
from . import views
from .views import UserListView

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
    path('users/', UserListView.as_view(), name='user_list'),

    path('categories/', views.category_list, name='category_list'),
]