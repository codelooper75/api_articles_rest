from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from celery.utils.log import get_task_logger
from scraper.views import scrape_posts
from celery import shared_task


logger = get_task_logger(__name__)


@shared_task
def scrape_posts_task():
    logger.info("Launched post scraper")
    return scrape_posts()