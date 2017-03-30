from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from shortener.models import KirrURL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, KirrURL):
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


@python_2_unicode_compatible
class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(KirrURL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return '{}'.format(self.count)
