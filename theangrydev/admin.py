from django.contrib import admin
from theangrydev.models import Post, Content, ContentType, Tag
# Register your models here.
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Content, admin.ModelAdmin)
admin.site.register(ContentType, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
