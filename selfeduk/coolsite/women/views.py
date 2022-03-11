from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse("Hello")


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Number <p>{catid}</p> </h1>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Archive by years<p>{year}<p/ </h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1>")
