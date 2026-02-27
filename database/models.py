from django.db import models
from django.forms import DateField


# Create your models here.

class Quote(models.Model):
    Quote=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)

    def __str__(self):
        return self.Quote


class DailyTasks(models.Model):

    status_choices = [("on progress","On progress"),("completed","Completed")]
    task_date=models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    status= models.CharField(max_length=200,choices=status_choices,default="on progress")

    def __str__(self):
        return self.title


class ComplteTasks(models.Model):
    task_date=models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    status= models.CharField(max_length=200)
    def __str__(self):
        return self.title


class MonthlyGoals(models.Model):
    status_choices = [("on progress","On progress"),("completed","Completed")]
    month=models.DateField()
    title=models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=status_choices, default="on progress")
    def __str__(self):
        return self.title

