from rest_framework import serializers
from Blog_Users.users.models import Blog, Comment, Category

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.StringRelatedField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'category', 'likes_count', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'content', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
