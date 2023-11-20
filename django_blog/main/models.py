from django.contrib.auth.models import User
from django.db import models
from rest_framework.authentication import TokenAuthentication


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ManyToManyField("Topic", related_name="article_topics")

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    subscribers = models.ManyToManyField(User, through="Preference")

    def __str__(self):
        return self.title


class Preference(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_notified = models.BooleanField(default=False)


class CustomTokenAuth(TokenAuthentication):
    keyword = 'Bearer'
