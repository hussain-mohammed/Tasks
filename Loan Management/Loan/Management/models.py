from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='')
    phone = models.IntegerField()
    dob = models.DateField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class LoanDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    duration = models.IntegerField(validators=[
            MaxValueValidator(30, "you cannot avail loan for more than 30 days")])
    STATUS = models.CharField(max_length=100, default="Available")
    returnedIN = models.IntegerField(default='0')
    amountPaid = models.IntegerField(default='0')


    def __str__(self):
        return self.user.username+' - '+self.STATUS
