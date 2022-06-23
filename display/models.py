from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="photo.jpg", upload_to="media", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} "

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            out_size = (300, 300)
            img.thumbnail(out_size)
            img.save(self.image.path)

class speak(models.Model):
    name = models.CharField(max_length=225)

class SMS(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    data = models.CharField(max_length=2084)
    image = models.ImageField(null=True, blank=True)
    time = models.DateTimeField(default=datetime.now, blank=True)


class Blog(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2083)
    time = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, related_name="blog_posts")

    def __str__(self):
        return f"{self.user.username}"

    @property
    def num_likes(self):
        return self.liked.all().count()


choice = (
    ("Like", "Like"),
    ("Unlike", "Unlike"),
)

class Like(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    value = models.CharField(choices=choice, default="Like", max_length=10)


class File(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to="save_file")

    def __str__(self):
        return self.user.username
