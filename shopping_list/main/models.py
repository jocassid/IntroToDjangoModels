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


class Item(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    store_type = models.ForeignKey(
        'StoreType',  # Can reference a table using a string
        null=True,  # No value stored as NULL in the database
        blank=True,  # Value is not required to save the record
        on_delete=models.SET_NULL,
        related_name='items',
    )

    def __repr__(self):
        return f"<Item: {self.name}>"

    def __str__(self):
        return self.name
