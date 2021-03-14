from django.db import models


class Videogames(models.Model):
    rank = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1000)
    platform = models.CharField(max_length=1000)
    year = models.IntegerField()
    genre = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=1000)
    na_sales = models.FloatField()
    eu_sales = models.FloatField()
    jp_sales = models.FloatField()
    other_sales = models.FloatField()
    global_sales = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.publisher}'


class DistinctPlatforms(models.Model):
    platform = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.platform}'

