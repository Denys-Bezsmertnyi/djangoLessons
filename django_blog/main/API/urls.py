from main.API.resources import ArticleViewSet, CommentViewSet, TopicViewSet, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'user', UserViewSet)
urlpatterns = router.urls
