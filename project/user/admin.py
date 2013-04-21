# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from project.user.forms import UserCreationForm, UserChangeForm
from project.user.models import User


class MyUserAdmin(UserAdmin):
    actions = None
    list_display = ('email', 'date_joined', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-id',)

    add_form = UserCreationForm
    form = UserChangeForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', )}),
        (_('Permissions'), {'fields': (
                        'is_active',
                        'is_staff',
                        'is_superuser',
                        #'groups', 'user_permissions'
            )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User, MyUserAdmin)
