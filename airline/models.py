from django.db import models


class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Airplane(BaseModel):
    airplane_id = models.PositiveIntegerField()
    passenger_assumptions = models.PositiveBigIntegerField()
