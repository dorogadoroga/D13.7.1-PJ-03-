from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug',)
    list_filter = ('slug',)
    search_fields = ('slug',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'title', 'category', 'image', 'media_content')
    list_filter = ('author', 'date', 'category')
    search_fields = ('author', 'date', 'title', 'category')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'post')
    list_filter = ('author', 'date', 'post')
    search_fields = ('author', 'date', 'post')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
