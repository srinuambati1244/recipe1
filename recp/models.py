from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Receipe(models.Model):
    receipe_name=models.CharField(max_length=300)
    id=models.IntegerField(primary_key=True)
    ingredients=models.CharField(max_length=270)
    process=models.CharField(max_length=300)
    images=models.ImageField(upload_to='image/')
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.receipe_name
