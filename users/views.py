from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from Blog_Users.users.models import Blog, Comment, Category
from Blog_Users.users.serializers import BlogSerializer, CommentSerializer, CategorySerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        blog = self.get_object()
        if request.user in blog.likes.all():
            blog.likes.remove(request.user)
            status = 'unliked'
        else:
            blog.likes.add(request.user)
            status = 'liked'
        return Response({'status': status})

    @action(detail=False, methods=['get'])
    def my_blogs(self, request):
        blogs = Blog.objects.filter(author=request.user)
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
