from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostsView.as_view(), name='posts'),
    path('posts/<int:post_id>/', views.PostView.as_view(), name='post')
]
