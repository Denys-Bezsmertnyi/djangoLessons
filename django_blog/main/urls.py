from django.urls import path, include
from main.API.urls import router

from .views import subscribe_to_topic, unsubscribe_from_topic, user_profile, set_password, set_userdata, \
    deactivate_account, Register, Login, Logout, TopicList, ArticleDetailVIew, CommentCreateView, AboutView, \
    ArticleCreateView, DeleteArticleView, ArticleUpdateView, ArticleListView

app_name = 'main'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', ArticleListView.as_view(), name="home_page"),
    path('about/', AboutView.as_view(), name="about"),
    path('<int:article_id>/', ArticleDetailVIew.as_view(), name="article"),
    path('<int:article_id>/add_comment/', CommentCreateView.as_view(), name="comment_create"),
    path('create/', ArticleCreateView.as_view(), name="create_article"),
    path('<int:article_id>/update/', ArticleUpdateView.as_view(), name="update_article"),
    path('<int:article_id>/delete/', DeleteArticleView.as_view(), name="delete_article"),
    path('topics/', TopicList.as_view(), name='topic_list'),
    path('topics/<int:topic>/subscribe/', subscribe_to_topic, name="subscribe_to_topic"),
    path('topics/<int:topic>/unsubscribe/', unsubscribe_from_topic, name="unsubscribe_from_topic"),
    path('profile/<str:username>/', user_profile, name="user_profile"),
    path('set-password/', set_password, name="set_password"),
    path('set-userdata/', set_userdata, name="set_userdata"),
    path('deactivate/', deactivate_account, name="deactivate_account"),
    path('register/', Register.as_view(), name="register_user"),
    path('login/', Login.as_view(), name="user_login"),
    path('logout/', Logout.as_view(), name="user_logout"),
]
