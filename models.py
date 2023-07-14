from tortoise import fields, models
# from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
# from tortoise.exceptions import *
# from tortoise.query_utils import Q
# from tortoise.transactions import atomic


class CargoType(models.Model):
    """Model for cargo type."""

    id = fields.IntField(pk=True)
    type = fields.CharField(max_length=50)

    # class Meta:
    #     table = 'cargo_types'

    # def __str__(self) -> str:
    #     return self.name


class DateRate(models.Model):
    """Model for rate assigned to date and cargo type."""

    id = fields.IntField(pk=True)
    date = fields.DateField(unique=True)
    cargo = fields.ForeignKeyField('models.CargoType', related_name='rates',
                                   on_delete=fields.RESTRICT)
    rate = fields.FloatField()

    class Meta:
        table = 'rates'
        unique_together = ('date', 'cargo')

