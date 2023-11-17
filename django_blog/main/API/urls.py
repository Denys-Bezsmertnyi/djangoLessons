from main.API.resources import ArticleViewSet, CommentViewSet, TopicViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'topics', TopicViewSet)

urlpatterns = router.urls
