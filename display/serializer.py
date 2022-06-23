from display.models import Blog
from rest_framework import serializers
from display.models import File

class BlogSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "user", "author", "title", "description", "time"]



class FileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "user", "file"]

