from django.contrib import admin

from .models import CronJob

# Register admin Posts
admin.site.register(CronJob)
