from django.shortcuts import render
from django.core.paginator import Paginator
from app_blog.models import Post, Slider, Category

# Create your views here.

def home(requet):
    ctx = {}
    ctx['Post'] = Post.objects.all().order_by("-date")
    ctx['Slider'] = Slider.objects.all().order_by("-id")
    return render(requet, 'home.html', ctx)

def post(request, slug):
    ctx = {}
    ctx['Post'] = Post.objects.get(slug=slug)
    ctx['Sug'] = Post.objects.all().order_by("-date").exclude(slug=slug)
    return render(request, 'post.html', ctx)

def archive(request):
    ctx = {}
    post_list = Post.objects.all().order_by("-date")
    paginator = Paginator(post_list, 7)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    ctx['Posts'] = posts
    return render(request, 'archive.html', ctx)

def categoryview(request, slug):
    ctx = {}
    post_list = Post.objects.all().order_by("-date").filter(category__slug=slug)
    category = Category.objects.get(slug=slug)
    paginator = Paginator(post_list, 7)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    ctx['Category'] = category
    ctx['Posts'] = posts
    return render(request, 'category.html', ctx)

