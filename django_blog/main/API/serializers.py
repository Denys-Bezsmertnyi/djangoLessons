from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import Article, Topic, Comment


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'subscribers']


class CommentReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'message', 'created', 'author']


class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'message', 'article', 'created']
        read_only_fields = ['author']


class ArticleReadSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField(many=True, read_only=True)
    comments = CommentReadSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created', 'updated', 'topic', 'comments', 'author']


class ArticleWriteSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created', 'updated', 'topic']
        read_only_fields = ['author']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(read_only=True, source='auth_token.key')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'password2', 'token']

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).count():
            raise ValidationError("User with this username already exists")

        if attrs['password'] != attrs['password2']:
            raise ValidationError("Passwords are different")
        attrs.pop('password2')
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, source='my_topics')
    articles = ArticleReadSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'topics', 'articles']


class UserSetPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("old_password", "new_password", "new_password2")

    def validate(self, attrs):
        if not self.instance.check_password(attrs['old_password']):
            raise ValidationError("Old password not valid")
        if attrs['new_password'] != attrs['new_password2']:
            raise ValidationError("New passwords are different")
        return attrs


class TopicSubscriptionSerializer(serializers.Serializer):
    subscribe = serializers.BooleanField(required=True)
