from django.utils import timezone


from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Users(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    objects = models.Manager()

    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.title


class Genre(models.Model):
    objects = models.Manager()
    GENRE = (
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Humor', 'Humor'),
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Detective', 'Detective'),
        ('Drama', 'Drama'),
        ('Adventure', 'Adventure'),
        ('Historical', 'Historical'),
        ('Tragedy', 'Tragedy')
    )

    genre = models.CharField(max_length=50, choices=GENRE)

    class Meta:
        ordering = ['genre']

    def __str__(self):
        return self.genre

#
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name



class Movies(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200, null=True)
    year = models.DateTimeField(null=True)
    released = models.DateTimeField(null=True)
    time = models.DateTimeField(null=True)
    description = models.CharField(max_length=500, null=True)
    genre = models.ManyToManyField(Genre, blank=True)
    images = models.ImageField(null=True, upload_to='images/')
    director = models.CharField(max_length=200, null=True)
    actors = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    production = models.CharField(max_length=200, null=True)
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True, auto_created=True)

    def get_avg_rating(self):
        rating = Rating.objects.filter(product=self)
        count = len(rating)
        sum = 1
        for rvw in rating:
            sum += rvw.rating
        return (sum / count)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.title)])

class Rating(models.Model):
    objects = models.Manager()
    product = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(max_length=200)

    def __str__(self):
        return str(self.product)+"---"+str(self.user)

class Comments(models.Model):
    object = models.Manager()
    created_date = models.DateTimeField(default=timezone.now, null=True)
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ['comment']

    def __str__(self):
        return self.comment



