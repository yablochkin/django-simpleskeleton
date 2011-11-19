# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from django.contrib.auth.models import User


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for constructor.
    """
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        self.columns = 2

        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            title=_(u'Быстрые ссылки'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_(u'Главная страница'), '/'],
                [_('Sentry'), reverse('sentry')]
            ]
        ))

        self.children.append(modules.AppList(
            title=_('Applications'),
            exclude_list=('django.contrib',),
        ))

        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5
        ))

        self.children.append(modules.Group(
            title=u'Статистика',
            display='tabs',
            children=[
                Summary(title=u'сводка'),
            ]
        ))

        self.children.append(modules.ModelList(
                title=u'Administration',
                include_list=[
                        'django.contrib.auth.*',
                    ],
            ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass

class Summary(modules.DashboardModule):

    template = 'dashboard/summary.html'

    def init_with_context(self, context):
        self.children = False # wtf? do not delete

        self.users = User.objects.count()
