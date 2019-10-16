from django.contrib import admin
from appName.models import *

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ["title","description","time"]
    list_filter = ["title"]
    search_fields = ["title"]

class NewsAdmin1(admin.ModelAdmin):
    list_display = ['label','decription']
    list_filter = ["label"]
    search_fields = ["label"]
admin.site.register(News,NewsAdmin)
admin.site.register(NewType,NewsAdmin1)