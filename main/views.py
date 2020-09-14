from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from json import dumps

from django.utils import translation
from django.utils.translation import gettext as _

def homepage(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    lang = translation.get_language()
    posts = Post.objects.all()

    if (lang == 'en'):
        titles = [x.title_EN for x in posts]
    elif (lang == 'de'):
        titles = [x.title_DE for x in posts]
    else:
        titles = [x.title_PT for x in posts]

    ids = [x.id for x in posts]
    images = [x.preview_image for x in posts]

    data = [(ids[i], titles[i], images[i]) for i in range(len(ids))]

    return render(
        request=request,
        template_name='main/home.html',
        context={
            'posts': data,
        }
    )

def post(request, post_id):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    currentPost = Post.objects.get(pk=post_id)
    lang = translation.get_language()

    if (lang == 'en'):
        dataDictionary = {'content': currentPost.content_EN}
        title = currentPost.title_EN
    elif (lang == 'de'):
        dataDictionary = {'content': currentPost.content_DE}
        title = currentPost.title_DE
    else:
        dataDictionary = {'content': currentPost.content_PT}
        title = currentPost.title_PT

    dataJSON = dumps(dataDictionary)

    return render(
        request=request,
        template_name='main/post.html',
        context={
            'title': title,
            'date': currentPost.date_published,
            'data': dataJSON,
        }
    )
