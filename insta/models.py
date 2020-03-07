from django.db import models
import datetime as dt

class Image(models.Model):
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =60)
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
