from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class KirrURL(models.Model):
    url = models.CharField(max_length=220, )

    def __str__(self):
        return str(self.url)
