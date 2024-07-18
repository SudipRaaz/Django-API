from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)

    # for testing this returns self
    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
