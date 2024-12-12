from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for posts with author-specific permissions.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response(
                {"detail": "You do not have permission to edit this post."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response(
                {"detail": "You do not have permission to delete this post."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for comments with author-specific permissions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.request.data.get("post"))
        serializer.save(author=self.request.user, post=post)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response(
                {"detail": "You do not have permission to edit this comment."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response(
                {"detail": "You do not have permission to delete this comment."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


class FeedView(generics.ListAPIView):
    """
    Displays posts from followed users in descending order of creation.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author__in=self.request.user.following.all()).order_by("-created_at")


class LikePostView(generics.GenericAPIView):
    """
    Allows users to like a post. Sends a notification to the post author.
    """
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response(
                {"detail": "You already liked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post,
        )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    """
    Allows users to unlike a post.
    """
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        like.delete()

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
