from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentBox


class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    paginate_by = 6
  

class Postinfo(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        return render(
            request,
            "open_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_box": CommentBox()

            }
        )

    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        
        comment_box = CommentBox(data=request.POST)
        if comment_box.is_valid():
            comment_box.instance.name = request.user.username
            comment = comment_box.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_box = CommentBox()

        return render(
            request,
            "open_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_box": comment_box,

            },
        )
