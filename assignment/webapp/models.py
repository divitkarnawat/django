from __future__ import unicode_literals
import csv
import io
from django.conf import settings
from django.db import models




class bank_details(models.Model):
    ifsc = models.CharField(max_length=50)
    bank_id = models.TextField(null=True)
    branch = models.TextField(null=True)
    address = models.TextField(null=True)
    city = models.TextField(null=True)
    district = models.TextField(null=True)
    state = models.TextField(null=True)
    bank_name = models.TextField(null=True)

    def __str__(self):
        return self.ifsc

