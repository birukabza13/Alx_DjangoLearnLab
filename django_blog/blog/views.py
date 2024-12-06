from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


class UserRegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "blog/login.html"


class UserLogoutView(LogoutView):
    template_name = "blog/logout.html"


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "blog/profile.html"
    model = User
    form_class = UserChangeForm
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.get_form()
            if form.is_valid():
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return super().post(request, *args, **kwargs)


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("post_list")


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    success_url = reverse_lazy("post_list")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    success_url = reverse_lazy("post_list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})


def search_posts(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(
        Q(title__icontains=query)
        | Q(content__icontains=query)
        | Q(tags__name__icontains=query)
    ).distinct()
    return render(request, "blog/search_results.html", {"posts": posts, "query": query})


def posts_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(request, "blog/posts_by_tag.html", {"posts": posts, "tag": tag})

class PostByTagListView(ListView):
    model = Post
    template_name = 'posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        tag = get_object_or_404(Tag, name=tag_name)

        return Post.objects.filter(tags=tag)