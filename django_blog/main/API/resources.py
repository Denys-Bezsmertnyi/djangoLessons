from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.API.permissions import IsAuthor
from main.API.serializers import TopicSerializer, ArticleSerializer, CommentSerializer, UserSerializer
from main.models import Article, Topic, Comment
from rest_framework import viewsets, mixins, status
from main.models import CustomTokenAuth
from django.contrib.auth.models import User


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [CustomTokenAuth]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            password = make_password(serializer.validated_data['password'])

            user = User.objects.create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                password=password
            )
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    @permission_classes([IsAuthenticated])
    def logout(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    @permission_classes([IsAuthenticated])
    def profile(self, request, pk):
        user = self.get_object()
        serializer = UserSerializer(user)
        topics = user.my_topics.all()[:10]
        topic_serializer = TopicSerializer(topics, many=True)
        article = user.articles.all()
        article_serializers = ArticleSerializer(article, many=True)
        return Response({'user': serializer.data,
                         'articles': article_serializers.data,
                         'topics': topic_serializer.data})

    @action(detail=True, methods=['put', 'patch'])
    @permission_classes([IsAuthenticated])
    def set_userdata(self, request, pk):
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put', 'patch'])
    @permission_classes([IsAuthenticated])
    def set_password(self, request, pk):
        user = self.get_object()
        new_password = request.data.get('password')

        if new_password:
            user.set_password(new_password)
            user.save()

            Token.objects.filter(user=user).delete()

            return Response({'detail': 'Password updated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'New password not provided.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    @permission_classes([IsAuthenticated])
    def deactivate(self, request, pk):
        user = self.get_object()
        user.delete()
        return Response({'message': 'Bye, bye :('}, status=status.HTTP_200_OK)
