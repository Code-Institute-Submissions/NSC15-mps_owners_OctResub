from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    car = models.CharField(max_length=200, default="Mazda")
    text = models.TextField()
    post_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_info", kwargs={"slug": self.slug})

class ThreadComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} commented {self.body}"