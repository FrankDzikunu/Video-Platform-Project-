from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title',)

admin.site.register(Video, VideoAdmin)
