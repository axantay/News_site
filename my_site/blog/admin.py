from django.contrib import admin

from .models import Category, Article, Customer


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'author', 'category', 'publish' )
    list_display_links = ('id', 'title')
    list_editable = ('content', 'author', 'category', 'publish')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'address', 'phone', 'github', 'instagram', 'x', 'facebook', 'website' )
    list_editable = ('first_name', 'last_name', 'address', 'phone', 'github', 'instagram', 'x', 'facebook', 'website')
    list_display_links = ('id', 'username')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Customer, CustomerAdmin)




