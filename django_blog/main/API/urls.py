from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from main.API.resources import ArticleViewSet, CommentViewSet, TopicViewSet, UserViewSet, LogoutApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),
    path('logout/', LogoutApiView.as_view())
]

