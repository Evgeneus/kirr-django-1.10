from __future__ import unicode_literals
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator()
    if not value.startswith('http://') and not value.startswith('https://'):
        value = 'http://' + value
    try:
        url_validator(value)
    except:
        raise ValidationError('Inavalid URL for this field')
    return value