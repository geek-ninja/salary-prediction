from django.db import models

# Create your models here.
class SalaryRecord(models.Model):
    experience = models.FloatField()
    salary     = models.FloatField()
    