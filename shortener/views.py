from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def kirr_redirect_view(request, *args, **kwargs):
    return HttpResponse('hello')


class KirrRedirectView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello again')
