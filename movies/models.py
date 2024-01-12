from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Movies(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(default='')
    cover=models.ImageField(upload_to='movies/')
    rating =models.FloatField(default=0.0)


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='rated_user')
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0,validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])
    review = models.CharField(max_length=250,null=True,blank=True)