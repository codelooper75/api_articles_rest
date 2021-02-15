from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from articles.models import *
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


import requests
from bs4 import BeautifulSoup



def scrape_posts():
    # if request.method == 'GET':
    req = requests.get('https://news.ycombinator.com/news?p=1')
    soup = BeautifulSoup(req.text, "lxml")


    posts = soup.find_all("a", class_="storylink")

    new_posts_count = 0 #is needed for response message
    for item in posts:
        title = str(item.get_text())
        url = item['href']

        #checking if post with this url already exist
        if not Article.objects.filter(url=url).count():
            # Saving posts to DB
            new_post = Article(title=title, url=url)
            new_post.save()
            new_posts_count += 1
    logger.info(f"new_posts: {new_posts_count}")
    return ({'status':'success','new_posts':new_posts_count})


