from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=30)
    abv = models.CharField(max_length=3, default="")
    rate = models.FloatField()
    rev_rate = models.FloatField(default=0)

    def __str__(self):
        return self.abv