from django.db import models

class Event(models.Model):

    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='events')
    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    attendees = models.ManyToManyField('Gamer', through='GamerEvent', related_name='attending')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
