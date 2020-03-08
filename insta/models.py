from django.db import models
import datetime as dt
from django.contrib.auth.models import User



class Image(models.Model):
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =60)
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
