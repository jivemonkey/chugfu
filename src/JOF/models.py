from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Movie info
class Movie(models.Model):
    title = models.CharField(max_length=300)
    releaseDate = models.DateField(null=True, blank=True)
    director = models.CharField(max_length=300, blank=True)
    imdbLink = models.CharField(max_length=300, blank=True)
    poster = models.TextField(max_length=300, blank=True)
    plot = models.TextField(blank=True)
    rated = models.TextField(max_length=20, blank=True)

# Review info   
class Review(models.Model):
    title = models.CharField(max_length=300)
    createDate = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True)
    movie = models.ForeignKey(Movie, related_name='reviews')
    user = models.ForeignKey(User, null=True, blank=True)

# Review rankings
class Ranking(models.Model):
    rating = models.FloatField()
    ratingType = models.CharField(max_length=300, blank=True)
    movie = models.ForeignKey(Movie, related_name='rankings')
    user = models.ForeignKey(User, blank=True)

# Site News
class News(models.Model):
    createDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    summary = models.TextField()

# Drinking Game
class Game(models.Model):
    title = models.CharField(max_length=300)
    createDate = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    movie = models.ForeignKey(Movie, related_name='games')
    user = models.ForeignKey(User, null=True, blank=True)

# Game Rule
class GameRule(models.Model):
    description = models.CharField(max_length=300)
    createDate = models.DateTimeField(auto_now_add=True)
    points = models.CharField(max_length=300)
    game = models.ForeignKey(Game, null=True, blank=True, related_name='rules')