from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from json import dumps

# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name='main/home.html',
        context={'posts': Post.objects.all}
    )

def post(request, post_id):
    currentPost = Post.objects.get(pk=post_id)
    dataDictionary = {'en': currentPost.content_EN, 'de': currentPost.content_DE, 'pt': currentPost.content_PT}
    dataJSON = dumps(dataDictionary)
    return render(
        request=request,
        template_name='main/post.html',
        context={
            'p': Post.objects.get(pk=post_id),
            'data': dataJSON,
        }
    )
