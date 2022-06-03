from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=200)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    # likes = models.ManyToManyField('like')
    comments = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.image
