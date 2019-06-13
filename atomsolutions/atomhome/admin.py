from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User

from django.contrib.auth.models import Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'content', 'owner', 'modified')

    


admin.site.register(Post, PostAdmin)
admin.site.site_header = 'Atom Solutions Admin'
admin.site.unregister(User)
admin.site.unregister(Group)
