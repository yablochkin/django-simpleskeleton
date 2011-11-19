# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
import uuid


def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    ext = ext.lower()
    name = uuid.uuid4().hex
    return 'entries/%s/%s.%s' % (instance.user.id, name, ext)

class Entry(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    title = models.CharField(_(u'Название'), max_length=160)
    url = models.URLField(_(u'URL'))
    created = models.DateTimeField(_(u'Дата создания'), auto_now_add=True)
    blocked = models.BooleanField(_(u'Заблокирован'), default=False)
    image = models.ImageField(_(u'Изображение'), upload_to=upload_path)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'сущность')
        verbose_name_plural = _(u'Сущности')

class Child(models.Model):
    entry = models.ForeignKey(Entry)
    title = models.CharField(_(u'Название'), max_length=160)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'дочерняя сущность')
        verbose_name_plural = _(u'Дочерние сущности')

def entry_save_handler(sender, instance, created, **kwargs):
    print instance.id

post_save.connect(entry_save_handler, sender=Entry)
