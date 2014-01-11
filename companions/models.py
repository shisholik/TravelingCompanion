from django.contrib.auth.models import User
from django.db import models

class City(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
      return self.title

class Route(models.Model):
    cityA = models.ForeignKey(City, related_name='routesA')
    cityB = models.ForeignKey(City, related_name='routesB')
    departureDate = models.DateTimeField('departure date')
    maxCompanions = models.IntegerField(default=4)
    description = models.CharField(max_length=400)
    creator = models.ForeignKey(User)
    users = models.ManyToManyField(User,related_name='users')
    def __str__(self):
      return self.description


class Companion(models.Model):
    route = models.ForeignKey(Route)
    user = models.ForeignKey(User)
    def __str__(self):
      return self.user.username +" " + self.route.__str__()