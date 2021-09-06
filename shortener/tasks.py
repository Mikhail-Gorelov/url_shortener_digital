import logging

from config.celery import app
from shortener.models import URL

logger = logging.getLogger(__name__)


@app.task
def delete_old_urls():
    try:
        result = URL.objects.filter(created__lt=URL.get_expiration_datetime()).delete()
        logger.info(f'delete_old_urls result: {result}')
    except Exception as ex:
        logger.exception(ex)
