# -*- coding: utf-8 -*-
from django.contrib import admin
from project.app.models import *


class EntryAdmin(admin.ModelAdmin):
    search_fields = ('user__email', 'title', )
    list_display = ('title', 'user', 'blocked', )
    raw_id_fields = ('user', )

class ChildAdmin(admin.ModelAdmin):
    list_display = ('title', 'entry', )
    raw_id_fields = ('entry', )

admin.site.register(Entry, EntryAdmin)
admin.site.register(Child, ChildAdmin)
