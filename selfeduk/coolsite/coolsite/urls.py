from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]

handler404 = 'women.views.pageNotFound'
#500 - server, 403 - privat
