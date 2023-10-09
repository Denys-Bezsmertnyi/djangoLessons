from django.urls import path
from .views import show_home_page, show_about, show_article, add_comment, create_article, update_article, \
    delete_article, list_topics, subscribe_to_topic, unsubscribe_from_topic, user_profile, set_password, set_userdata, \
    deactivate_account, register_user, user_login, user_logout

urlpatterns = [
    path('', show_home_page, name="home_page"),
    path('about/', show_about, name="about"),
    path('<int:article_id>/', show_article, name="article"),
    path('<int:article_id>/comment/', add_comment, name="add_comment"),
    path('create/', create_article, name="create_article"),
    path('<int:article_id>/update/', update_article, name="update_article"),
    path('<int:article_id>/delete/', delete_article, name="delete_article"),
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
