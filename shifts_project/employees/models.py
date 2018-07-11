from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class EmployeeManager(models.Manager):
  def get_queryset(self):
    return super(Employee, self).get_queryset().filter(city='London')

class Employee(models.Model):
  user = models.OneToOneField(User)
  city = models.CharField(max_length=100, null=True, blank=True)
  phone = models.IntegerField(null=True, blank=True)
  wage = models.IntegerField(default=0)

  def __str__(self):
    return self.user.username

def create_profile(sender, **kwargs):
  if kwargs['created']:
    employee_profile = Employee.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
