from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify


# Create your models here.

# Catagory model

class Catagory(models.Model):
    #catagories = ["Food", "Artificial Intelligence", "Data Science", "Games", "Sports"]
    catagories = models.CharField(max_length=100)

    def __str__(self):
        return self.catagories

#post Model

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.URLField(null=True)
    created_at_time = models.DateTimeField(auto_now_add=True)
    slugs = models.SlugField(unique=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slugs = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

