import datetime
import logging
import random
import string

from django.conf import settings
from django.db import models, IntegrityError

from config.settings import URLS_TTL

logger = logging.getLogger(__name__)


def generate_short_url():
    return ''.join(random.choice(string.ascii_letters) for i in range(6))


class URL(models.Model):
    session = models.CharField('Session key', max_length=255)
    url = models.URLField('Original URL', max_length=3000)
    short_url = models.SlugField('Short URL', max_length=255, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session

    @staticmethod
    def get_expiration_datetime():
        if not URLS_TTL:
            return datetime.datetime.min
        return datetime.datetime.now()-datetime.timedelta(seconds=URLS_TTL)

    def get_short_url(self):
        return f'{settings.HOST}/{self.short_url}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.short_url:
            self.short_url = generate_short_url()

        try:
            super().save()
        except IntegrityError as ex:
            ex_message = str(ex)
            if ex_message == 'UNIQUE constraint failed: shortener_url.short_url':
                logger.error(ex_message)
                return self.save()
            raise IntegrityError(ex_message)