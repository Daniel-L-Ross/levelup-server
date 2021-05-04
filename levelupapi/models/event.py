from django.db import models

class Event(models.Model):

    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    date = models.DateField
    time = models.TimeField
    address = models.CharField
    attendees = models.ManyToManyField('Gamer', through='GamerEvent')
