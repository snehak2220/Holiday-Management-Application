from django.db import models

# Create your models here.
class Holiday(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    holiday_type = models.CharField(max_length=255)
    country = models.CharField(max_length=2)
    year = models.IntegerField()


    def __str__(self):
        return f"{self.name} {self.country}({self.date})"