from django.contrib import admin
from .models import Post
from django.contrib.admin import ModelAdmin

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_filter = ('car', 'created_on')
    list_display = ('title', 'author', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
