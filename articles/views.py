from django.shortcuts import render
from rest_framework import generics
from articles.serializers import *
from articles.models import *
# from django_filters import filters
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet




class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListlSerializer
    queryset = Article.objects.all()


    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'id']


