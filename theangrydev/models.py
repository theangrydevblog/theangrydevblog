from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

from uuid import uuid4
# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=100, default=f"{str(uuid4()).split('-').pop()}")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    @property
    def is_admin(self):
        return self.admin

    def has_module_perms(self, app_label):
        return True

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

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
