from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Item(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField(
        validators=[MinValueValidator(0)],
        verbose_name='Weight in kg'
    )

    def __str__(self):
        return self.name


class Inventory(models.Model):
    user = models.OneToOneField(User)
    items = models.ManyToManyField(Item)

    class Meta:
        verbose_name_plural = 'inventories'

    def __str__(self):
        return "{}'s inventory".format(self.user.username)
