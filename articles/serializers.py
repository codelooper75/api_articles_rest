from rest_framework import serializers
from articles.models import Article

class ArticleListlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title','url','created')


