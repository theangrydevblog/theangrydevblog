from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    draft = models.BooleanField()
    published = models.DateField()

    def __str__(self):
        return self.title

class ContentType(models.Model):
    name = models.CharField(max_length=100)
    metadata = JSONField(null=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.post.title} {self.type.name} {self.timestamp}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name="tags")

    def __str__(self):
        return self.name
