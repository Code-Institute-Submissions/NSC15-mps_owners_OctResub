from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Post, ThreadComment
from .forms import CommentBox, EditComment
from django.views.generic import UpdateView


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
            messages.success(self.request, 'Your comment has been added')
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
class UpdateComment(UpdateView):
    model = ThreadComment
    template_name = 'edit_comment.html'
    form_class = CommentBox
