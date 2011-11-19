# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from simplereg.forms import LoginForm


urlpatterns = patterns('',
    url(r'^$', 'project.app.views.hello', name='hello'),
    url(r'^faq/$', TemplateView.as_view(template_name='faq.html'), name='faq'),

    #url(r'^entry/create/$', 'project.adnet.app.create_entry', name='create_entry'),
    #url(r'^entry/edit/(?P<campaign_id>\d+)/$', 'project.adnet.app.edit_entry', name='edit_entry'),

    url(r'^registration/advert/$', 'simplereg.views.registration', {
            'template_name': 'common/registration.html',
            'callback': None
        }, name='registration'),

    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {
            'template_name': 'common/password_change.html'
        }, name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', {
            'template_name': 'common/password_change_done.html'
        }, name='password_change_done'),

    url(r'^login/$', 'django.contrib.auth.views.login', {
        'authentication_form': LoginForm,
            'template_name': 'common/login.html'
        }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
            'next_page': '/'
        }, name='logout'),
)
