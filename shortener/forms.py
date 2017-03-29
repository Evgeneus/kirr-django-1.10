from django import forms

from .validators import validate_url


class SabmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url])

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Inavalid URL for this field')
    #     return url
