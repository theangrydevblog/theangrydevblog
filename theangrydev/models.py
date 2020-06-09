from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.template.defaultfilters import slugify
from django.urls import reverse
from .managers import UserManager

from uuid import uuid4
from faker import Faker

fake_name_generator = Faker()
# Create your models here.

class User(AbstractBaseUser):
    def random_username():
        return fake_name_generator.name().replace(" ","").lower()

    email = models.EmailField(unique=True)
    avatar = models.CharField(max_length=75, default="https://api.adorable.io/avatars/40/e1f2c206-ceda-447c-a81c-0b164def.png")
    username = models.CharField(max_length=100, default=random_username)
    uuid = models.UUIDField(default=uuid4)

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
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    def add_vote(self, user, vote):
        self.vote_set.create(
            user=user,
            post=self,
            type=vote
        )

    # We don't want to just disassociate the vote but completely delete it
    def remove_vote(self, user):
        vote_by_user = Vote.objects.filter(user=user, post=self).first()
        vote_by_user.delete()

    @property
    def upvotes(self):
        return len(self.vote_set.filter(type=True))

    @property
    def downvotes(self):
        return len(self.vote_set.filter(type=False))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

# This makes upvoting/downvoting strictly ACID
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.BooleanField()

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return f"{self.user} : {self.post} : {self.type}"


class ContentType(models.Model):
    name = models.CharField(max_length=100)
    metadata = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    timestamp = models.DateField(default=timezone.now)
    rank = models.IntegerField(default=0)
    metadata = JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.post.title} {self.type.name} {self.timestamp}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000, blank=True)
    posts = models.ManyToManyField(Post, related_name="tags")

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'name': self.name})

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscriber} -> {self.tag}"

class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.email} : {self.timestamp}"
