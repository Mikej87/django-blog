from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
# Register your models here.


admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    # This creates the table columns you see in the list
    list_display = ('author', 'body', 'post', 'created_on', 'approved')


class AboutAdmin(admin.ModelAdmin):
    """
    Displays the About model in the admin panel
    and allows user to edit the content.
    """
    list_display = ('title', 'updated_on')
