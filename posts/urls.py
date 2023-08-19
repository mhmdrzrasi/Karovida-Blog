from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('posts/<int:post_id>/', views.PostView.as_view(), name='post'),
    path('posts/demo/', views.PostsDemoView.as_view(), name='posts-demo'),
    path('posts/<int:post_id>/demo/', views.PostDemoView.as_view(), name='post-demo'),
]
