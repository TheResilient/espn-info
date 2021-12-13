from django.db import models

# Create your models here.

# class Player(models.Model):
#     name = models.TextField()
#     type = models.TextField()
#     age = models.IntegerField()
#     batting_h = models.TextField()
#     bowling_h = models.TextField()

#     def __str__(self):
#         return self.name

class Squad(models.Model):
    name = models.TextField()
    # player = models.ForeignKey(Player,on_delete=models.CASCADE)

class match(models.Model):
    match_id = models.IntegerField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
