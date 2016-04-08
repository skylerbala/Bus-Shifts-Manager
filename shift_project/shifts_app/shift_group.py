from django.db import models


class ShiftGroupManager(models.Manager):
    pass


class ShiftGroup(models.Model):

    #shifts_related

    db_table="shift_group"
    objects = ShiftGroupManager()

    class Meta:
        app_label = "shifts_app"