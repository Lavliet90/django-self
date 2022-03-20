from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'id_publisher')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('id_publisher',)
    list_filter = ('id_publisher', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'id_publisher', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 50>")

    get_html_photo.short_description = 'Photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Women\'s site admin panel'

admin.site.site_header = 'Women\'s site admin panel.'
