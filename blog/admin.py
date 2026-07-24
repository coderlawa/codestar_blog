from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'status', 'created_on')
    search_fields = ['title', 'author__username', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('body', 'author', 'approved', 'post', 'created_on')
    search_fields = ['post__title', 'author__username', 'body']
    list_filter = ('approved', 'created_on')
    summernote_fields = ('body',)