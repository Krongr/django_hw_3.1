from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=40)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    release_date = models.CharField(max_length=40)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
