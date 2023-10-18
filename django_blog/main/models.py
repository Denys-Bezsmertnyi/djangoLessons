from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ManyToManyField("Topic")

    def get_absolute_url(self):
        return reverse('main:article', args=[str(self.pk)])


class Topic(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    subscribers = models.ManyToManyField(User, through="Preference")


class Preference(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_notified = models.BooleanField(default=False)
