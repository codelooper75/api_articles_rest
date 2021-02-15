from django.contrib import admin
from django.urls import path, include
from scraper.views import *

urlpatterns = [
    path('update/', scrape_posts),
]
