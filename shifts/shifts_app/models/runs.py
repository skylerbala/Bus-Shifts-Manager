from django.db import models
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from django.db.models import Q

class TimeStampedModel(models.Model):
  start_datetime = models.DateTimeField()
  end_datetime = models.DateTimeField()

  class Meta:
    abstract = True

class Run(TimeStampedModel):
    shift = models.ForeignKey('Shift', on_delete=models.CASCADE)
    user_id = models.IntegerField(default=0, blank=True)

    class Meta:
        app_label = "shifts_app"
        db_table="run"

