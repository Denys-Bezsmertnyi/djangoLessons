from django.contrib import admin

from .models import Article, Topic, Comment, Preference

admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Preference)
