from django.contrib import admin
from theangrydev.models import (
    Post,
    Content,
    ContentType,
    Tag,
    User,
    Comment,
    Subscription,
    Vote
)
# Register your models here.
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Content, admin.ModelAdmin)
admin.site.register(ContentType, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(User, admin.ModelAdmin)
admin.site.register(Comment, admin.ModelAdmin)
admin.site.register(Subscription, admin.ModelAdmin)
admin.site.register(Vote, admin.ModelAdmin)
