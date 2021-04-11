from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

import urllib.parse

from .models import Choice, Question, Url

def Index(request):
    return render(request, 'polls/UrlShortener.html', {})

def url_shortener(request):
    short_url = request.GET["url"]
    try:
        url = Url.objects.get(url=short_url)
    except Url.DoesNotExist:
        url = Url(url=urllib.parse.unquote(short_url))
        url.save()
    return JsonResponse('https://url-shortener-310004.et.r.appspot.com/'+encode(url.id)+'/redirect/', safe=False)

def redirect(request, short):
    print(short)
    print(decode(short))
    url = get_object_or_404(Url, pk=decode(short))
    return render(request, 'polls/redirect.html', {'short_url' : url.url})

temp = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num):
    global temp

    if num == 0:
        return temp[0]

    base = len(temp)
    short = ''

    while num:
        num, rem = divmod(num, base)
        short = temp[rem] + short

    return short


def decode(short):
    global temp

    num = 0

    for char in short:
        num = num * 62
        num += temp.index(char)

    return num