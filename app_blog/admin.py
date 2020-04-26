from django.contrib import admin
from app_blog.models import Post, Category, Slider

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'main_content', "category__title"]

admin.site.register(Post, PostAdmin)
admin.site.register(Slider)
admin.site.register(Category)
admin.site.site_header = 'مدیریت Rghaf.ir'