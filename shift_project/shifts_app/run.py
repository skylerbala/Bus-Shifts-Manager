from django.db import models

from shifts_app.shift import Shift

class RunManager(models.Manager):
    
   def check_overlap(self, runs):

        shift_times = [(shift.start_datetime, shift.end_datetime) for shift in shifts_to_cover]

        for time_range in set(shift_times):
            
            users_conflicting_shifts = Shift.objects.filter(
                    #covers any time range encapsulating the start or end datetimes of the user's shifts
                    ((Q(runs_related__start_datetime__range=time_range) & Q(runs_related__end_datetime__range=time_range) )
                    |
                    #covers a start_time within or equal to the user's shift start_datetime and end_datetime
                    #also covers an end_time within or equal to the user's shift start_datetime and end_datetime
                    (Q(runs_related__start_datetime__lte=time_range[0]) & Q(runs_related__end_datetime__gte=time_range[1]) )),

                    runs_related__jobs_related__current_resp__user=user
                )

            if users_conflicting_shifts.exists():
                #yes overlap
                return True

        #no overlap
        return False       


class Run(models.Model):

    db_table="run"
    objects = RunManager()

    shift = models.ForeignKey(Shift, related_name="runs_related")

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        app_label = "shifts_app"