from django.db import models
from django.contrib.auth import get_user_model #лучше делать так, чем наследоваться он нее напрямую, т.к. она может быть переопределена

class Article(models.Model):
    title = models.CharField(verbose_name='Title', max_length=512)
    url = models.CharField(verbose_name='URL', unique=True, max_length=512)
    created = models.DateTimeField(auto_now_add=True)
