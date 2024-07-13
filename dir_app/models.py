from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Creator(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    
    profile_picture = models.ImageField()
    
    
class How_it_works(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    class Meta:
        verbose_name_plural = 'How_it_works'
    
class Explore(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    rated_count = models.IntegerField()
    price = models.CharField(max_length=255)
    typee = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='Explore')
    posted_by = models.ForeignKey(Creator, on_delete=models.CASCADE)
    
class Client_reviews(models.Model):
    client = models.ForeignKey(Creator, on_delete=models.CASCADE)
    adress = models.CharField(max_length=255)
    body = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Client_reviews'
    
class Reviews(models.Model):
    listing = models.IntegerField()
    listing_categories = models.IntegerField()
    visitors = models.IntegerField()
    happy_clients = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Reviews'
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Creator, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    img = models.ImageField(upload_to='Blog')
    
    
class About_web(models.Model):
    owner = models.ForeignKey(Creator, on_delete=models.CASCADE)
    call_center = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    class Meta:
        verbose_name = 'About web'
    
