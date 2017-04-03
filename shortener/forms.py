from __future__ import unicode_literals
from django import forms

from .validators import validate_url


class SabmitUrlForm(forms.Form):
    url = forms.CharField(label='',
                          validators=[validate_url],
                          widget=forms.TextInput(
                              attrs={"placeholder": "Long URL",
                                     "class": "form-control"}
                          ))

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Inavalid URL for this field')
    #     return url
