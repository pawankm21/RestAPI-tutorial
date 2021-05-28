from django.db import models
from django.db.models.fields import DateField

# Create your models here.
# this is our model
class Loan(models.Model):
    typeof = models.CharField(max_length=50)
    agent= models.CharField(max_length=50)
    starting_date= models.DateField(blank=True)
    ending_date= models.DateField(blank=True)
    interest_rate=models.IntegerField()

    def __str__(self):
        return self.typeof


