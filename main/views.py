from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name='main/home.html',
        context={'posts': Post.objects.all}
    )

def article(request, article_id):
    return render(
        request=request,
        template_name='main/article.html',
        context={'p': Post.objects.get(pk=article_id)}
    )

def about(request):
    return render(
        request=request,
        template_name='main/about.html'
    )
