from django.shortcuts import render, get_object_or_404,
reverse
from django.views import generic
from .models import Post
from django.contrib import messages
from django.http import HttpResponseRedirect
from about.models import Comment
from .forms import CommentForm


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

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
        )

    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()
    print("About to render template")

    return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "comment_form": comment_form,
                "coder": "Matt Rudge"
            },
        )


def event_detail(request, event_id):
        # This is a placeholder for your future event view
    return render(request, "blog/event_detail.html", {"event_id": event_id})
