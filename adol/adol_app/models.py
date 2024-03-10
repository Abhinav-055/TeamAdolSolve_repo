from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_tasks = models.ManyToManyField(Task, blank=True)