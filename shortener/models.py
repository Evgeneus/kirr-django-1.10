from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from .utils import create_shortcode


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURL, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_codes_count = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes_count += 1
        return '{} shortсodes are updated'.format(new_codes_count)


@python_2_unicode_compatible
class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
