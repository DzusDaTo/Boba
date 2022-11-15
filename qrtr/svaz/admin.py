from django.contrib import admin
from .models import *


class SvazAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'sposob', 'create_at', 'otvet')
    list_display_links = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name', 'create_at', 'otvet')
    list_filter = ('last_name', 'first_name', 'create_at', 'otvet')
    readonly_fields = ('create_at',)
    list_editable = ('otvet',)
    fields = ('last_name', 'first_name', 'sposob', 'create_at', 'pravki', 'otvet')


admin.site.register(Svaz, SvazAdmin)
