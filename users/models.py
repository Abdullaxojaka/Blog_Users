from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_blogs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'
