from django.db import models

class CousreModel(models.Model):
     idno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=50,unique=True)
     fee = models.IntegerField()

class CommonModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cnnum = models.IntegerField(unique=True)
    subject = models.CharField(max_length=50)

    class Meta:
        abstract = True
class StudentModel(CommonModel):
    subject = models.ManyToManyField(CousreModel)
    marks = models.FloatField()

class FacuiltyModel(CommonModel):
    subject = models.ManyToManyField(CousreModel)
    salary = models.FloatField()
