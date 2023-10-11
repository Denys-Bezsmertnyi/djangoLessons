from django.http import HttpResponse
from django.shortcuts import render


def show_article(request, article_id):
    return render(request, 'main/post/detail.html')


def show_home_with_categories(request):
    category_list = ["Anime", "Cartoon", "Horror", "Sci-fi", "Novell"]
    return render(request, 'main/post/list.html', {'category_list': category_list})


def show_about(request):
    return render(request, 'main/about.html')


def add_comment(request, article_id):
    return render(request, 'main/post/add_comment.html')


def create_article(request):
    return render(request, 'main/post/create_article.html')


def update_article(request, article_id):
    return render(request, 'main/post/update_article.html')


def delete_article(request, article_id):
    return render(request, 'main/post/delete_article.html')


def topic_list(request):
    return render(request, 'main/topic/topic_list.html')


def subscribe_to_topic(request, topic):
    return render(request, 'main/topic/topic_subscribe.html')


def unsubscribe_from_topic(request, topic):
    return render(request, 'main/topic/topic_unsubscribe.html')


def user_profile(request, username):
    return render(request, 'main/user/profile.html')


def set_password(request):
    return render(request, 'main/user/set_password.html')


def set_userdata(request):
    return render(request, 'main/user/set_userdata.html')


def deactivate_account(request):
    return render(request, 'main/user/deactivate.html')


def register_user(request):
    return render(request, 'main/user/register.html')


def user_login(request) -> HttpResponse:
    return render(request, 'main/user/login.html')


def user_logout(request):
    return render(request, 'main/user/logout.html')
