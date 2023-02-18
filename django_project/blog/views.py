from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.jinja2'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.jinja2'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.jinja2'
    context_object_name = 'post'


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'blog/new_post.jinja2'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.jinja2'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_url = '/'
    success_message = "Post Deleted Succesfully"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def about(request):
    return render(request, 'blog/about.jinja2', context={'title': 'about'})
