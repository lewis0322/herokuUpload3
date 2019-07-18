from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    contents = models.TextField()
    lookup = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title