from django.db import models
from django.template.defaultfilters import slugify


class ClothType(models.Model):
    type = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.type


class Clothes(models.Model):
    what_size = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("X", "X"),
        ("XL", "XL"),
    ]

    name = models.CharField(max_length=40, blank=False)
    slug = models.SlugField(null=True)
    brand = models.CharField(max_length=64, blank=True)
    size = models.CharField(max_length=3, choices=what_size, null=True, blank=True)
    description = models.TextField(default="", blank=True)
    photo = models.ImageField(upload_to="photos", blank=True, null=True)
    cloth_type = models.ForeignKey(ClothType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
