from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.contrib.admin.options import ModelAdmin
from django.db import models

from .models import Article, Comment


# Register your models here.
admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "author", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]

    class Meta:
        model = Article
