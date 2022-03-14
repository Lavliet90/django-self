from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
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
        'cat_selected': 0,
    }
    return render(request, "women/index.html", context=context)


def about(request):
    return render(request, "women/about.html", {'title': 'About us', "menu": menu})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Error add article')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Add article'})


def contact(request):
    return HttpResponse('hi')


def login(request):
    return HttpResponse('hi')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)
    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Categories',
        "menu": menu,
        'posts': posts,
        'cat_selected': cat_slug,
    }
    return render(request, "women/index.html", context=context)


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
