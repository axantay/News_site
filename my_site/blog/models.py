from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from my_site import settings



class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, blank=True)
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Article(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name='Заголовок')
    content = models.TextField(default='нет ничего', verbose_name='Toliq')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновленная дата')
    image = models.ImageField(blank=True, upload_to='images/', verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    publish = models.BooleanField(default=True, verbose_name='Распечатать')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)


    def get_photo(self):
        if self.image:
            return self.image.url
        else:
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT8-e9Jpr1AyNwkdf_iE_zQjknFwrn3kBbQQ&s"

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'



class Customer(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, blank=True, verbose_name='Телефон номер')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Аддресс')
    website = models.URLField(blank=True, null=True, verbose_name='Сайт')
    github = models.CharField(max_length=255, blank=True, verbose_name='Github')
    x = models.CharField(max_length=255, blank=True, verbose_name='X')
    instagram = models.CharField(max_length=255, blank=True, verbose_name='Instagram')
    facebook = models.CharField(max_length=255, blank=True, verbose_name='Facebook')


    REQUIRED_FIELDS = [ 'phone', 'address', 'website', 'github', 'x', 'instagram', 'facebook']


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'





class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


















