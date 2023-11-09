from django.db import models

# Create your models here.
class Copa_Libertadores(models.Model):
    continent= models.CharField(max_length=100)
    season=models.IntegerField()
    champion= models.CharField(max_length=250)
    runner_up= models.CharField(max_length=250)
    best_player= models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.champion}, {self.runner_up}'

class Copa_Sudamericana(models.Model):
    continent= models.CharField(max_length=100)
    season=models.IntegerField()
    champion= models.CharField(max_length=250)
    runner_up= models.CharField(max_length=250)
    best_player= models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.champion}, {self.runner_up}'

class Champions_League(models.Model):
    continent= models.CharField(max_length=100)
    season=models.IntegerField()
    champion= models.CharField(max_length=250)
    runner_up= models.CharField(max_length=250)
    best_player= models.CharField(max_length=250, blank=True)

    def __str__(self): 
        return f'{self.champion}, {self.runner_up}'