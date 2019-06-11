from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    exclude = ('author', )
    list_display = ('owner', 'title', 'content', 'created', 'modified')

    # def has_change_permission(self, request, obj=None):
    #     has_class_permission = super(
    #         PostAdmin, self).has_change_permission(request, obj)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
    #         return False
    #     return True

    # def queryset(self, request):
    #     if request.user.is_superuser:
    #         return Post.objects.all()
    #     return Post.objects.filter(author=request.user)

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.owner = request.user
    #     obj.save()


admin.site.register(Post, PostAdmin)
admin.site.site_header = 'Atom Solutions Admin'
