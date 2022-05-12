from django.db import models


class student (models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=30)
    studcourse = models.CharField(max_length=20)
    staff = models.CharField(max_length=30)
    chapter = models.IntegerField()
    mychoice=[('yes','yes'),('no','no')]
    present = models.CharField(max_length=5,choices=(mychoice))
    date = models.DateTimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.stuid},{self.stuname},{self.studcourse},{self.staff},{self.chapter},{self.present},{self.date},{self.duration}'
class staff (models.Model):
    stuid = models.IntegerField(primary_key=True)
    evaluation_date = models.DateTimeField()
    def __str__(self):
        return f'{self.stuid},{self.evaluation_date}'
