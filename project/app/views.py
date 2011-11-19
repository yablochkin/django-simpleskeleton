# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from project.app.models import Entry
from json import dumps
import datetime


def hello(request):
    #messages.success(request, _(u'Регистрация прошла успешно. Теперь можно перейти к созданию вашего первого объявления.'))
    return direct_to_template(request, 'app/hello.html', {
            'title': 'hello world'
        })

@login_required
def edit(request, entry_id):
    entry = get_object_or_404(Entry, id=campaign_id, user=request.user)
    form = CampaignForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        messages.success(request, _(u'Кампания изменена успешно.'))
        return redirect(campaigns)
    return direct_to_template(request, 'app/edit_entry.html', {
            'form': form
        })
