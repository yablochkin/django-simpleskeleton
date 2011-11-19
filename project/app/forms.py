# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django import forms
from project.app.models import Entry


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'image')

class TestForm(forms.Form):
    name = forms.CharField(label=_(u'Имя'), max_length=50)
    surname = forms.CharField(label=_(u'Фамилия'), max_length=50)
