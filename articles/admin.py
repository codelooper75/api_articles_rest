from django.contrib import admin
from articles.models import Article
from django.utils.safestring import mark_safe

@admin.register(Article)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "created") #колонки которые будут видны в админке
    list_display_links = ("title",) #по чему кликать, что бы провалиться внутрь
    # list_filter = ("user",)  # фильтрация по чему
    search_fields = ("title", "url" )






admin.site.site_title = "Article API"
admin.site.site_header = "Article API" #меняет заголовок в админке