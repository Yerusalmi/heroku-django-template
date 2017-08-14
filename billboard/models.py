# Create your models here.

from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    message = models.CharField(max_length=300)


    def __str__(self):
        return self.title
