from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.CharField(max_length=200, default="Mazda")
    text = models.TextField()
    post_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.title