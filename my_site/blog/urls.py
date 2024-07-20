from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='index'),
    path('', ArticleList.as_view( ), name='index'),
    # path('category/<int:pk>/', category_items, name='category'),
    path('category/<int:pk>/', ArticlesByCategory.as_view(), name='category'),
    # path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('article/<int:pk>/delete/', DeleteArticle.as_view(), name='delete_article'),
    path('article/<int:pk>/update/', EditArticle.as_view(), name='update'),
    path('search/', search, name='search'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
    path('profile/', profile, name='profile'),
    path('add_comment/<int:article_id>', save_comment, name='save_comment'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),


]