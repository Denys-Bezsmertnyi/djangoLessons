from django.urls import path
from .views import *

urlpatterns = [
    path('', show_home_page, name="home_page"),
    path('about/', show_about, name="about"),
    path('<int:article>/', show_article, name="article"),
    path('<int:article>/comment/', add_comment, name="add_comment"),
    path('create/', create_article, name="create_article"),
    path('<int:article>/update/', update_article, name="update_article"),
    path('<int:article>/delete/', delete_article, name="delete_article"),
    path('topics/', list_topics, name="list_topics"),
    path('topics/<int:topic>/subscribe/', subscribe_to_topic, name="subscribe_to_topic"),
    path('topics/<int:topic>/unsubscribe/', unsubscribe_from_topic, name="unsubscribe_from_topic"),
    path('profile/<str:username>/', user_profile, name="user_profile"),
    path('set-password/', set_password, name="set_password"),
    path('set-userdata/', set_userdata, name="set_userdata"),
    path('deactivate/', deactivate_account, name="deactivate_account"),
    path('register/', register_user, name="register_user"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
]
