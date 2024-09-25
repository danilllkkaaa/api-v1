from django.db import models


class Main(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
