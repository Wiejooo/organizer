from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Sizes(models.Model):
    type = models.CharField(max_length=64, blank=False)
    cm_value = models.IntegerField(blank=False, default=0)
    overall = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.type


class ClothType(models.Model):
    type = models.CharField(max_length=64, blank=False)
    measurement = models.ManyToManyField(Sizes, blank=True)
    slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.type


class ClothSubType(models.Model):
    type = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.type

class Marketplaces(models.Model):
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    what_size = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("X", "X"),
        ("XL", "XL"),
    ]

    name = models.CharField(max_length=40, blank=False, unique=True)
    slug = models.SlugField(null=True, unique=True)
    brand = models.CharField(max_length=64, blank=True)
    size = models.CharField(max_length=3, choices=what_size, null=True, blank=True)
    purchase_price = models.FloatField(blank=False, default=0)
    predicted_sale_price = models.FloatField(blank=False, default=0)
    sold_price = models.FloatField(blank=False, default=0)
    condition = models.IntegerField(blank=False, null=False, default=5, validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    description = models.TextField(default="", blank=True)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    marketplaces = models.ManyToManyField(Marketplaces, blank=True)
    cloth_type = models.ForeignKey(ClothType, null=True, on_delete=models.SET_NULL)
    cloth_sub_type = models.ForeignKey(ClothSubType, null=True, on_delete=models.SET_NULL)
    sell_statute = models.BooleanField("Sold", default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        elif self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    @property
    def description_generator(self):
        """Funkcja do generowania opisów"""

        return f"""
FOLLOW MY SHOP AND FEEL FREE TO FAVORITE LISTINGS IF YOU LIKE REGULAR ITEM UPDATES AND PRICE DROPPERS
        """

    @property
    def description_generator_2(self):
        """Funkcja do generowania opisów"""

        return f"""
Size {self.size} Recommend checking the measurements as sizes might occasionally vary
Condition used, overall condition {self.condition}/10, wear is evident. Please look over all of the pictures.

See also SIZE Measurements
"""

    @property
    def description_generator_3(self):
        """Funkcja do generowania opisów"""

        return f"""
___________________________________
Accepting bids. updates to the goods every day.
Tracked shipment from Poland to all countries.
Always sending 48 hours after payment.
Typically shipping takes 9 - 16 business days to arrive. {self.marketplaces}
"""
