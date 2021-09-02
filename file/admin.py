from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Filemodel)
class FileAdmin(admin.ModelAdmin):
    class Meta:
        search_fields = ('author', 'name')
        list_display = (
        'author', 'name', 'created_date','expiration_date'
        )
@admin.register(CommentModel)
class Commentadmin(admin.ModelAdmin):
    class Meta:
        search_fields = ('author', 'comment_date')
        list_display = (
        'author', 'comment_date'
        )
@admin.register(ShareModel)
class ShareAdmin(admin.ModelAdmin):
    class Meta:
        search_fields = ('sender', 'reveiver')
        list_display = (
        'sender', 'receiver'
        )