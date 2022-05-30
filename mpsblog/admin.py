from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Post, ThreadComment


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_filter = ('car', 'created_on')
    list_display = ('title', 'author', 'created_on')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(ThreadComment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('post', 'name')
