from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth import logout, login
from django.db.models import Q
from django.urls import reverse_lazy

from .forms import ArticleForm, CommentForm, UserLoginForm, UserRegisterForm
from .models import *


# def index(request):
#     categories = Category.objects.all()
#     articles = Article.objects.all()
#     context = {
#         'categories': categories,
#         'title': "News",
#         'articles': articles
#     }
#     return render(request, 'blog/index.html', context)
class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/index.html'  # blog/article_list.html
    extra_context = {
        'title': "Class",

    }

    def get_queryset(self):
        return Article.objects.filter(publish=True)


# def category_items(request, pk):
#     category = Category.objects.get(pk=pk)
#     articles = Article.objects.filter(category=category)
#     context = {
#         'title': category.title,
#         'articles': articles,
#
#     }
#     return render(request, 'blog/index.html', context)

class ArticlesByCategory(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['pk'], publish=True)


# def article_detail(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'title': article.title,
#         'article': article,
#     }
#     return render(request, 'blog/article_detail.html', context)


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['title'] = article.title
        context['comments'] = Comment.objects.filter(article=article)
        context['comment_form'] = CommentForm()
        return context


class AddArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'


def profile(request):
    context = {
        'title': "Профиль",

    }
    return render(request, 'blog/profile.html', context)


def save_comment(request, article_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = Article.objects.get(pk=article_id)
        comment.save()
    else:
        pass

    return redirect('article_detail', article_id)


def user_logout(request):
    logout(request)
    return redirect('index')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'title': "Войти"

    }

    return render(request, 'blog/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'title': "Регистрация",
        'form': form
    }

    return render(request, "blog/register.html", context)


class DeleteArticle(DeleteView):
    model = Article
    success_url = reverse_lazy('index')
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(DeleteArticle, self).get_context_data()
        context['title'] = "Удалить текст"
        return context


class EditArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'


def search(request):
    word = request.GET.get('q')
    articles = Article.objects.filter(Q(title__icontains=word)|Q(content__icontains=word), publish=True)
    context = {
        'title': word,
        'articles': articles
    }
    return render(request, 'blog/index.html', context)
