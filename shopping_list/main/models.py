from django.db import models


class StoreType(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    def __repr__(self):
        return f"<StoreType: {self.name} ({self.pk})>"

    def __str__(self):
        return self.name


class Store(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    types = models.ManyToManyField(
        StoreType,
        related_name='stores',
    )

    def __repr__(self):
        return f"<Store: {self.name} ({self.pk})>"

    def __str__(self):
        return self.name
