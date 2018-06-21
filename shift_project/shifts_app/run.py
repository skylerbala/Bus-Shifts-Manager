from django.db import models
from shifts_app.shift import Shift


class Run(models.Model):
    db_table="run"

    shift = models.ForeignKey('Shift', on_delete=models.CASCADE)
    user_id = models.IntegerField(default=0, blank=True)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        app_label = "shifts_app"