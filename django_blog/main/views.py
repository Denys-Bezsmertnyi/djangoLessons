from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import AddCommentForm
from .models import Article, Comment, Topic


def topic_list(request):
    topics = Topic.objects.all()
    return render(request,
                  'main/topic/topic_list.html',
                  {'topics': topics})


@login_required(login_url='/login/')
def show_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = article.comment_set.all()
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            article = Article.objects.get(pk=article_id)
            author = request.user
            Comment.objects.create(message=message, author=author, article=article)
            return redirect(reverse('main:article', args=[article_id]))
    else:
        form = AddCommentForm()
    return render(request, 'main/post/detail.html', {'form': form,
                                                     'article': article,
                                                     'comments': comments})


def home_page(request):
    if request.method == 'GET':
        topic_id = request.GET.get('topic_id')

        if topic_id:
            topic = Topic.objects.get(pk=topic_id)
            articles = topic.article_topics.all()
            topics = Topic.objects.all()
            return render(request,
                          'main/post/list.html',
                          {
                              'articles': articles,
                              'topic': topic,
                              'topics': topics})
        else:
            articles = Article.objects.all()
            topics = Topic.objects.all()
            return render(request,
                          'main/post/list.html', {
                              'articles': articles,
                              'topics': topics})


def show_about(request):
    return render(request, 'main/about.html')


@login_required(login_url='/login/')
def create_article(request):
    return render(request, 'main/post/create_article.html')


@login_required(login_url='/login/')
def update_article(request, article_id):
    return render(request, 'main/post/update_article.html')


@login_required(login_url='/login/')
def delete_article(request, article_id):
    return render(request, 'main/post/delete_article.html')


def topic_list(request):
    return render(request, 'main/topic/topic_list.html')


@login_required(login_url='/login/')
def subscribe_to_topic(request, topic):
    return render(request, 'main/topic/topic_subscribe.html')


@login_required(login_url='/login/')
def unsubscribe_from_topic(request, topic):
    return render(request, 'main/topic/topic_unsubscribe.html')


@login_required(login_url='/login/')
def user_profile(request, username):
    return render(request, 'main/user/profile.html')


@login_required(login_url='/login/')
def set_password(request):
    return render(request, 'main/user/set_password.html')


@login_required(login_url='/login/')
def set_userdata(request):
    return render(request, 'main/user/set_userdata.html')


@login_required(login_url='/login/')
def deactivate_account(request):
    return render(request, 'main/user/deactivate.html')


class Register(CreateView):
    template_name = 'main/user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main:home_page')


class Login(LoginView):
    template_name = 'main/user/login.html'
    success_url = reverse_lazy('main:home_page')

    def get_success_url(self):
        return self.success_url


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'
