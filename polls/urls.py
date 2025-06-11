from django.urls import path
from . import views
from .views import UserListView

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
    path('users/', UserListView.as_view(), name='user_list'),

    path('categories/', views.category_list, name='category_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]