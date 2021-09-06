from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, redirect

from shortener.forms import URLForm
from shortener.services import get_or_create_session_key, ShortenerService


def main(request):
    context = {}
    session_key = get_or_create_session_key(request.session)

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url_object = form.save(session_key=session_key)
            cache.set(url_object.short_url, url_object.url, timeout=settings.CACHE_TTL)
            form = URLForm()
    else:
        form = URLForm()

    paginated_urls = ShortenerService().get_paginated_urls(session_key, request.GET.get('page'))

    context['form'] = form
    context['paginated_urls'] = paginated_urls
    return render(request, 'shortener/main.html', context)


def redirect_to_origin(request, short_url):
    original_url = ShortenerService().get_original_by_short_or_404(short_url)
    return redirect(original_url)
