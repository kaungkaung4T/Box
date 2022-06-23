from django.contrib import admin
from display.models import profile
from display.models import speak
from display.models import SMS
from display.models import Blog, File
from display.models import File, Like

# Register your models here.
class SpeakAdmin(admin.ModelAdmin):
    list_display = ("name",)

class SMSAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "data", "image", "time")

class BlogAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "description", "time")

class FileAdmin(admin.ModelAdmin):
    list_display = ("user", "file")


admin.site.register(speak, SpeakAdmin)
admin.site.register(SMS, SMSAdmin)
admin.site.register(profile)
admin.site.register(Blog, BlogAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Like)