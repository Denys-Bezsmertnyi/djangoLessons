from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Article, Topic, Comment
from main.forms import AddCommentForm, ArticleCreateForm


class ArticleFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            email='test_user@gmail.com',
            password='top_secret'
        )
        self.topic = Topic.objects.create(title='Test Topic', description='Test Description')

    def test_article_create_form(self):
        form_data = {'title': 'Test Article', 'content': 'Test content', 'topic': [self.topic.id]}
        form = ArticleCreateForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_article_create_form_without_title(self):
        form_data = {'content': 'Test content', 'topic': [self.topic.id]}
        form = ArticleCreateForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())

    def test_article_create_form_without_topic(self):
        form_data = {'title': 'Test Article', 'content': 'Test content'}
        form = ArticleCreateForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('topic', form.errors.keys())

    def test_article_create_form_with_invalid_topic(self):
        form_data = {'title': 'Test Article', 'content': 'Test content', 'topic': [999]}
        form = ArticleCreateForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('topic', form.errors.keys())


class CommentFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            email='test_user@gmail.com',
            password='top_secret'
        )
        self.topic = Topic.objects.create(title='Test Topic', description='Test Description')

    def test_add_comment_form(self):
        form_data = {'message': 'Test message'}
        form = AddCommentForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_add_comment_form_without_message(self):
        form_data = {}
        form = AddCommentForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())

