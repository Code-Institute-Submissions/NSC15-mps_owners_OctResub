from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, ThreadComment
from .forms import CommentBox


class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    paginate_by = 6


class Postinfo(LoginRequiredMixin, View):

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
            messages.error(self.request, 'Your comment couldnt be added')

        return render(
            request,
            "open_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_box": comment_box,

            },
        )


class UpdateComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ThreadComment
    fields = ['body']
    template_name = 'edit_comment.html'
    success_url = "/"
    success_message = "Comment successfully changed"


class DeleteComment(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ThreadComment
    template_name = 'delete_comment.html'

    def get_success_url(self):
        messages.success(self.request, "Your comment was deleted successfully")
        return '/'
