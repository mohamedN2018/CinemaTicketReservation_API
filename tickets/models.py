from django.db import models

# Create your models here.


# gust -- Movie -- Reservation


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Movies'
        verbose_name = 'Movie'

    def __str__(self):
        return self.movie

class Guest(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Guests'
        verbose_name = 'Guest'

    def __str__(self):
        return self.name


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = 'Reservations'
        verbose_name = 'Reservation'

    def __str__(self):
        return f"Reservation for {self.guest} - {self.movie}"