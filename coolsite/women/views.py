from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': 'About us', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_page'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        ]


def index(request):
    posts = Women.objects.all()
    context = {
        'title': 'Main page',
        "menu": menu,
        'posts': posts,
    }
    return render(request, "women/index.html", context=context)


def about(request):
    return render(request, "women/about.html", {'title': 'About us', "menu": menu})


def addpage(request):
    return HttpResponse('hi')


def contact(request):
    return HttpResponse('hi')


def login(request):
    return HttpResponse('hi')

def show_post(request, post_id):
    return HttpResponse(f'Отображение сиаити {post_id}')


# def categories(request, catid):
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f"<h1>Number <p>{catid}</p> </h1>")
#
#
# def archive(request, year):
#     if int(year) > 2022:
#         return redirect('home', permanent=True)
#
#     return HttpResponse(f"<h1>Archive by years<p>{year}<p/ </h1>")
#

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1>")
