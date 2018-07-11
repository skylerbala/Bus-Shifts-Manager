from django.db import models

class Run(models.Model):
    shift = models.ForeignKey('Shift', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

