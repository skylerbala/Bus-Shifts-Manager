from django.db import models
import string
class Run(models.Model):
    shift = models.ForeignKey('Shift', related_name='run_set', on_delete=models.CASCADE)
    line = models.CharField(max_length=1)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def get_unique_lines(self):
        return Run.objects.distinct('line')