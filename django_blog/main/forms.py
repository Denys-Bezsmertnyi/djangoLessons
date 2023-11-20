from django import forms

from main.models import Comment, Article, Topic


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        if 'article_id' in kwargs:
            self.article_id = kwargs.pop('article_id')
        self.user = kwargs.pop('user', None)
        super(AddCommentForm, self).__init__(*args, **kwargs)


class ArticleCreateForm(forms.ModelForm):
    topic = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topic.objects.all(),
    )

    class Meta:
        model = Article
        fields = ['title', 'content', 'topic']

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ArticleCreateForm, self).__init__(*args, **kwargs)
