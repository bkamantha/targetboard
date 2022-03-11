from django.db import models


class LeanBand(models.Model):
    BandId = models.AutoField(primary_key=True)
    TLID = models.CharField(max_length=10)
    GLID = models.CharField(max_length=10)


class ModuleTarget(models.Model):
    HeadID = models.AutoField(primary_key=True)
    TDate = models.DateField()
    LBId = models.CharField(max_length=15)
    Shift = models.CharField(max_length=2)
    Style = models.CharField(max_length=15)
    Size = models.CharField(max_length=15)
    planhour = models.IntegerField()
    potenetialhour = models.CharField(max_length=15)
    hour1 = models.IntegerField(null=True)
    hour2 = models.IntegerField(null=True)
    hour3 = models.IntegerField(null=True)
    hour4 = models.IntegerField(null=True)
    hour5 = models.IntegerField(null=True)
    hour6 = models.IntegerField(null=True)
    hour7 = models.IntegerField(null=True)
    hour8 = models.IntegerField(null=True)
    hour9 = models.IntegerField(null=True)
    hour10 = models.IntegerField(null=True)
    hour11 = models.IntegerField(null=True)
    hour12 = models.IntegerField(null=True)

    hour1re = models.IntegerField(null=True)
    hour2re = models.IntegerField(null=True)
    hour3re = models.IntegerField(null=True)
    hour4re = models.IntegerField(null=True)
    hour5re = models.IntegerField(null=True)
    hour6re = models.IntegerField(null=True)
    hour7re = models.IntegerField(null=True)
    hour8re = models.IntegerField(null=True)
    hour9re = models.IntegerField(null=True)
    hour10re = models.IntegerField(null=True)
    hour11re = models.IntegerField(null=True)
    hour12re = models.IntegerField(null=True)


class Downtime(models.Model):
    DTId = models.AutoField(primary_key=True, default=True)
    DTDate = models.DateField(null=False)
    LBID = models.CharField(max_length=10, default=None)
    Shift = models.CharField(max_length=10, null=False)
    HeadNo = models.CharField(max_length=10, null=False)
    StartTime = models.TimeField(null=False)
    EndTime = models.TimeField(null=False)
    DTCode = models.CharField(max_length=10, null=False)
    Status = models.CharField(max_length=10, default=None)
