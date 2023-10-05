from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def show_home_page(request):
    return HttpResponse("This is homepage")


def show_about(request) -> HttpResponse:
    return HttpResponse("About text")


def show_article(request: HttpRequest, article) -> HttpResponse:
    return HttpResponse(f"Article text{article = }")


def add_comment(request, article) -> HttpResponse:
    return HttpResponse("Add comment here")


def create_article(request) -> HttpResponse:
    return HttpResponse("Article create")


def update_article(request, article) -> HttpResponse:
    return HttpResponse("Article update")


def delete_article(request, article) -> HttpResponse:
    return HttpResponse("Article delete")


def list_topics(request) -> HttpResponse:
    return HttpResponse("Topics list")


def subscribe_to_topic(request, topic) -> HttpResponse:
    return HttpResponse("Subscribe to topic")


def unsubscribe_from_topic(request, topic) -> HttpResponse:
    return HttpResponse("Unsubscribe from topic")


def user_profile(request, username) -> HttpResponse:
    return HttpResponse("User profile")


def set_password(request) -> HttpResponse:
    return HttpResponse("Set password")


def set_userdata(request) -> HttpResponse:
    return HttpResponse("Set userdata")


def deactivate_account(request) -> HttpResponse:
    return HttpResponse("Account deactivate")


def register_user(request) -> HttpResponse:
    return HttpResponse("Register user")


def user_login(request) -> HttpResponse:
    return HttpResponse("User login")


def user_logout(request) -> HttpResponse:
    return HttpResponse("User logout")
