from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'anons', 'get', 'create_at', 'is_published')
    list_display_links = ('title', 'anons')
    search_fields = ('title', 'anons', 'create_at', 'is_published')
    list_filter = ('title', 'anons', 'image', 'is_published')
    readonly_fields = ('create_at', 'get',)
    list_editable = ('is_published',)
    fields = ('title', 'anons', 'image', 'get', 'file', 'create_at', 'is_published', 'views')

    def get(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=150")

    get.short_description = 'Миниатюра'


class IPAdmin(admin.ModelAdmin):
    list_display = ('ip',)


admin.site.register(Ip, IPAdmin)

admin.site.register(Video, VideoAdmin)
