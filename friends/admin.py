from django.contrib import admin
from .models import Friends


class FriendsAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend', 'status']


admin.site.register(Friends, FriendsAdmin)
