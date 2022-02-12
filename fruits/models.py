from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=20)
    color = models.ForeignKey(
        'Color',
        related_name='fruits',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField()

class Color(models.Model):
    name = models.CharField(max_length=20)