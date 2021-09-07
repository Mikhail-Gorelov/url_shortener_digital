from django.conf import settings
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from shortener.models import URL


def get_or_create_session_key(session):
    if not session.session_key:
        session.create()
    return session.session_key


class ShortenerService:
    @staticmethod
    def get_original_by_short_or_404(short_url):
        original_url = cache.get(short_url)
        if not original_url:
            url_object = get_object_or_404(URL, short_url=short_url)
            original_url = url_object.url
            cache.set(short_url, original_url, timeout=settings.CACHE_TTL)
        return original_url

    @staticmethod
    def get_paginated_urls(session_key, page):
        urls = URL.objects.filter(session=session_key).order_by('-created')
        return Paginator(urls, 10).get_page(page)
