from django.contrib import admin
from app_blog.models import Post, Category, Slider

# Register your models here.

admin.site.register(Post)
admin.site.register(Slider)
admin.site.register(Category)