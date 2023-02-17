from django.urls import path
from blog import views

urlpatterns = [
    path("", views.PostListView.as_view(), name='blog-home'),
    path("home/", views.PostListView.as_view(), name='blog-home'),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name='post-detail'),
    path("home/post/<int:pk>/", views.PostDetailView.as_view(), name='post-detail'),
    path("post/new/", views.PostCreateView.as_view(), name='post-detail'),
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name='post-update'),
    path("home/post/<int:pk>/update",
         views.PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name='post-delete'),
    path("home/post/<int:pk>/delete",
         views.PostDeleteView.as_view(), name='post-delete'),
    path("post/new/", views.PostCreateView.as_view(), name='post-detail'),
    path("home/post/new/", views.PostCreateView.as_view(), name='post-detail'),
    path("about/", views.about, name='blog-about'),
]
