from django.db import models

# Create your models here.

class bookModels(models.Model):
    book_id = models.IntegerField()
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    ratings = models.DecimalField(max_digits=2, decimal_places=1,blank=True,null=True)
    genre = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

