from django.db import models

class Game(models.Model):

    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()