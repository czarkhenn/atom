from django.contrib import admin
from .models import Post, Postjp
from django.contrib.auth.models import User

from django.contrib.auth.models import Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'content', 'owner', 'modified')

class PostjpAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'content', 'owner', 'modified')
    


admin.site.register(Post, PostAdmin)
admin.site.register(Postjp, PostjpAdmin)
admin.site.site_header = 'Atom Solutions Admin'
admin.site.unregister(User)
admin.site.unregister(Group)
