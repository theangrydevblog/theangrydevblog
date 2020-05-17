from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from theangrydev.models import (
    Post,
    Content,
    ContentType,
    Tag,
    User,
    Comment,
    Subscription,
    Vote,
    Message
)
# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm

    list_display = ('email', 'username')
    list_filter = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields':('username',
                            'avatar')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Content, admin.ModelAdmin)
admin.site.register(ContentType, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, admin.ModelAdmin)
admin.site.register(Subscription, admin.ModelAdmin)
admin.site.register(Vote, admin.ModelAdmin)
admin.site.register(Message, admin.ModelAdmin)
