from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.urls import reverse



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

    def get_absolute_url(self):
        return reverse('index')

    @classmethod
    def search_by_title(cls,search_term):
        insta = cls.objects.filter(title__name__icontains=search_term)
        return insta

class Comment(models.Model):
    post = models.ForeignKey('insta.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
