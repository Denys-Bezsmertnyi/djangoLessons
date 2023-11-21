from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, TemplateView, DeleteView, UpdateView

from .forms import AddCommentForm, ArticleCreateForm
from .models import Article, Topic


class TopicList(ListView):
    template_name = 'main/topic/topic_list.html'
    context_object_name = 'topics'
    queryset = Topic.objects.all()


class ArticleDetailVIew(DetailView):
    model = Article
    pk_url_kwarg = 'article_id'
    template_name = 'main/post/detail.html'
    extra_context = {'form': AddCommentForm()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(pk=self.object.pk)
        comments = article.comments.all()
        context['comments'] = comments
        return context


class ArticleListView(ListView):
    template_name = 'main/post/list.html'
    queryset = Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()
        topics = Topic.objects.all()
        topic_id = self.request.GET.get('topic_id')

        if topic_id:
            topic = Topic.objects.get(pk=topic_id)
            articles = topic.article_topics.all()
            topics = Topic.objects.all()
        context['articles'] = articles
        context['topics'] = topics
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ['post']
    form_class = AddCommentForm
    pk_url_kwarg = 'article_id'
    login_url = reverse_lazy('main:user_login')

    def get_success_url(self):
        article = self.object.article
        return article.get_absolute_url()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request, "article_id": self.kwargs.get('article_id'), "user": self.request.user})
        return kwargs

    def form_invalid(self, form):
        return HttpResponseRedirect(self.success_url)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.message = form.cleaned_data['message']
        comment.article = Article.objects.get(pk=form.article_id)
        comment.author = form.user
        comment.save()
        return super().form_valid(form=form)


class AboutView(TemplateView):
    template_name = 'main/about.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('main:user_login')
    http_method_names = ['get', 'post']
    form_class = ArticleCreateForm
    template_name = 'main/post/create_article.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request, "user": self.request.user})
        return kwargs

    def form_invalid(self, form):
        return HttpResponseRedirect(self.success_url)

    def form_valid(self, form):
        article = form.save(commit=False)
        article.title = form.cleaned_data['title']
        article.author = form.user
        article.content = form.cleaned_data['content']
        article.save()
        article.topic.set(form.cleaned_data['topic'])
        return super().form_valid(form=form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('main:user_login')
    model = Article
    pk_url_kwarg = 'article_id'
    template_name = 'main/post/update_article.html'
    fields = ['title', 'content', 'topic']


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('main:home_page')
    login_url = reverse_lazy('main:user_login')
    pk_url_kwarg = 'article_id'
    template_name = 'main/post/confirm_delete.html'


@login_required(login_url='/login/')
def subscribe_to_topic(request, topic):
    return render(request, 'main/topic/topic_subscribe.html')


@login_required(login_url='/login/')
def unsubscribe_from_topic(request, topic):
    return render(request, 'main/topic/topic_unsubscribe.html')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'main/user/profile.html'
    login_url = reverse_lazy('main:user_login')
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.object.pk)
        topics = user.my_topics.all()[:3]
        context['topics'] = topics
        articles = user.articles.all()
        context['articles'] = articles
        return context


class UserdataUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('main:user_login')
    model = User
    pk_url_kwarg = 'user_id'
    template_name = 'main/user/set_userdata.html'
    fields = ['username', 'first_name', 'last_name']

    def get_success_url(self):
        return reverse_lazy('main:user_profile', kwargs={'user_id': self.object.pk})


class UserChangePassword(LoginRequiredMixin, PasswordChangeView):
    login_url = reverse_lazy('main:user_login')
    pk_url_kwarg = 'user_id'
    template_name = 'main/user/set_password.html'
    model = User
    fields = ['password']

    def get_success_url(self):
        return reverse_lazy('main:user_profile', kwargs={'user_id': self.request.user.pk})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'main/user/deactivate.html'
    login_url = reverse_lazy('main:user_login')
    pk_url_kwarg = 'user_id'
    success_url = reverse_lazy('main:home_page')

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
