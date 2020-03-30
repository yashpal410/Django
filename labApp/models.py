'''
    writing model classes for creating Tables
    '''

from datetime import datetime as dt
from django.db import models
# Create your models here.
class User(models.Model):
    ''' creating User Table '''
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)
    def __str__(self):
        return self.id

class ActivityPeriod(models.Model):
    ''' Creating ActivityPeriod Table '''
    idm = models.CharField(max_length=9)
    start_time = models.DateTimeField(default=dt.now(), blank=True)
    end_time = models.DateTimeField(default=dt.now(), blank=True)
    def __str__(self):
        return self.idm
