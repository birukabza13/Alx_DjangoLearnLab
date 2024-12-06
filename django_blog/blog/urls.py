from .views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
    UserProfileView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    posts_by_tag,
    search_posts,
    PostByTagListView,
)
from django.urls import path

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile_page"),
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_edit"),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"
    ),
    path("search/", search_posts, name="search_posts"),
    path("tags/<name:tag_name>/", PostByTagListView.as_view()),
]
