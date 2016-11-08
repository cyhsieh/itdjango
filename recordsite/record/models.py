from django.db import models

# Create your models here.



class Subject(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Record(models.Model):
    datetime = models.DateTimeField()
    subject = models.ForeignKey(Subject)
    content = models.CharField(max_length=30)
    duration = models.DecimalField(max_digits=3, decimal_places=0, blank=True)
    note = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.datetime + self.subject