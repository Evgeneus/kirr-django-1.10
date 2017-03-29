from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from .forms import SabmitUrlForm
from .models import KirrURL


class KirrRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SabmitUrlForm()
        context = {
            'title': 'Submit URL',
            'form': the_form
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SabmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('url'))
        context = {
            'title': 'Submit URL',
            'form': form
        }
        return render(request, 'shortener/home.html', context)
