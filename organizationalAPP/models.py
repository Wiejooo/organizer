from django.db import models


class Clothes(models.Model):
    what_size = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('X', 'X'),
        ('XL', 'XL'),
    ]

    name = models.CharField(max_length=64, blank=False)
    brand = models.CharField(max_length=64, blank=True)
    size = models.CharField(max_length=3, choices=what_size)
    description = models.TextField(default='', blank=True)
    when_both = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name
