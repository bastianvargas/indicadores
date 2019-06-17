import uuid
from django.db import models


class Currency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    value = models.FloatField(default=None)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'currencies'
