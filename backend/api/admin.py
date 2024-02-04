from django.contrib import admin
from .models import User,VideoModel
# Register your models here.

class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'description')
admin.site.register(User)
admin.site.register(VideoModel,VideoModelAdmin)

