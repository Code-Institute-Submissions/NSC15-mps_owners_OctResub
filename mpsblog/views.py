from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    paginate_by = 6
    
class Postinfo(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "open_post.html",
            {
                "post": post
            }
        )

