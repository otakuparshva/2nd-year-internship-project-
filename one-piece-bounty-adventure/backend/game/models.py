from django.db import models

# Create your models here.
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
