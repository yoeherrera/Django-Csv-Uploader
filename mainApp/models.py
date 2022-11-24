from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    marks = models.PositiveIntegerField(default=0)
    roll_number = models.PositiveIntegerField(default=0)
    section = models.CharField(max_length=50)