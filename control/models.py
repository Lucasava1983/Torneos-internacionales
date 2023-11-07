from django.db import models

# Create your models here.
class Copa_Libertadores(models.Model):
    continent= models.CharField(max_length=100)
    season=models.IntegerField()
    champion= models.CharField(max_length=250)
    runner_up= models.CharField(max_length=250)
    best_player= models.CharField(max_length=250, blank=True)

class Copa_Sudamericana(models.Model):
    continent= models.CharField(max_length=100)
    season=models.IntegerField()
    champion= models.CharField(max_length=250)
    runner_up= models.CharField(max_length=250)
    best_player= models.CharField(max_length=250, blank=True)

class Champions_League(models.Model):
    continent= models.CharField(max_length=100)
    season=models.IntegerField()
    champion= models.CharField(max_length=250)
    runner_up= models.CharField(max_length=250)
    best_player= models.CharField(max_length=250, blank=True)