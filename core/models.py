from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
