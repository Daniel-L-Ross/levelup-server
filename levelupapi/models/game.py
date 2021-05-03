from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=50)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)