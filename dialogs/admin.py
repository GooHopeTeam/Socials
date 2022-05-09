from django.contrib import admin
from .models import Dialog, Message


@admin.register(Dialog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend', 'created', 'updated')


@admin.register(Message)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('dialog', 'message', 'sender')
