from django.contrib import admin

from . import models


class CommentInLine(admin.TabularInline):
    model = models.Comment

class NewsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Comment)