from django.contrib import admin
from .models import Profile, Society, SocietyMembers, SocietyComments

admin.site.register(Profile)
admin.site.register(Society)
admin.site.register(SocietyMembers)
admin.site.register(SocietyComments)
