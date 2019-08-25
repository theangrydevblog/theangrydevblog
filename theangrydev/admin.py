from django.contrib import admin
from theangrydev.models import Post, Content, ContentType
# Register your models here.
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Content, admin.ModelAdmin)
admin.site.register(ContentType, admin.ModelAdmin)
