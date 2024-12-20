from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'content']  # Allows filtering by title and content
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    @action(detail=False, methods=['get'], url_path='feed')
    def feed(self, request):
        # Get posts from users the current user follows
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
