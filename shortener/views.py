from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from .forms import SabmitUrlForm
from .models import KirrURL
from analytics.models import ClickEvent


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
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
            new_url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'
        else:
            template = 'shortener/home.html'
            context = {
                'title': 'Inavalid URL. Try again :)',
                'form': form
            }

        return render(request, template, context)
