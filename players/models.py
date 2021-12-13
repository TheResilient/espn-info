from django.db import models

class Squad(models.Model):
    name = models.TextField()

class match(models.Model):
    match_id = models.IntegerField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
