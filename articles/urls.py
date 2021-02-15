from django.contrib import admin
from django.urls import path, include
from articles.views import *


urlpatterns = [
    path('', ArticleListView.as_view()),
]
