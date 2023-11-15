from rest_framework import serializers

from main.models import Article, Topic, Comment


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'subscribers']


class ArticleSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created', 'updated', 'author', 'topic']


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'created', 'message', 'author', 'article']
