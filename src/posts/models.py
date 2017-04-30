from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts_created')
    content = models.CharField(max_length=140)
    created_time = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.content


class HashTag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

