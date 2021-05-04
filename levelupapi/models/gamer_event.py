from django.db import models

class Gamer_event(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)