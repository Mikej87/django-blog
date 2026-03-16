from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from about.models import About

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    context_object_name = "post_list"  
    paginate_by = 6

def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user to view them.
    """
    about = About.objects.all().order_by('-updated_on').first()
    return render(
        request,
        "about/about.html",
        {"about": about},
    )

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "coder": "Matt Rudge"
        },
    )

def event_detail(request, event_id):
    # This is a placeholder for your future event view
    return render(request, "blog/event_detail.html", {"event_id": event_id})
