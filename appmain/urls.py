from django.urls import path
from django.contrib.auth.views import LoginView
from appmain.views import get_books
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

appname="appmain"


urlpatterns = [
    # URL untuk halaman pendaftaran
    path('', views.show_main, name='show_main'),
    path('login/', views.login_user, name='login'),
    path('adminregister/', views.admin_register, name='admin_register'),
    path('userregister/', views.user_register, name='user_register'),
    path('logout/', views.logout_user, name='logout'),
    path('adminmenu/', views.admin_menu, name='admin_menu'),
    path("get_books/",get_books, name="get_books"),
    path('forum/', PostListView.as_view(), name='forum-home'),
    #path('forum/about/', views.forum_about, name='forum-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Tambahkan URL lainnya sesuai kebutuhan
]