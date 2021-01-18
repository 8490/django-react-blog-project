from django.contrib import admin
from .models import Category, Post, PostView, Like, Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Comment)

