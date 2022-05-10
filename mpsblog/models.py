from django.db import models


class CreateUser(models.Model):
    name = models.CharField(max_length=20, help_text='Enter your name')
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=30, help_text='Enter your home town location')

    def __str__(self):
        return self.name