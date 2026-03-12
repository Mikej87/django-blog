from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by =6

    