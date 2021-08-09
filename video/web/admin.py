from django.contrib import admin

# Register your models here.
from web.models import Video, Img, ImgCategory, VideoCategory, Music


class MusicPollAdmin(admin.ModelAdmin):
    list_display = ('name','file')


admin.site.register(Video)
admin.site.register(VideoCategory)
admin.site.register(Img)
admin.site.register(ImgCategory)
admin.site.register(Music, MusicPollAdmin)
# admin.site.register([Music])
