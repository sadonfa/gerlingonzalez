from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):

    entradas = Post.objects.filter(published=True)

    return render(request, "blog.html", {
        'title': 'Blog',
        'entradas': entradas
    })

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    return render(request, 'blog/category.html',{
        'category': category
    })

def article(request, id, art_slug):

    article = Post.objects.get(id=id)

    return render(request, 'article.html', {
        'article': article
    })