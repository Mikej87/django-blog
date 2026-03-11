from django.contrib import admin
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # This creates the table columns you see in the list
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
