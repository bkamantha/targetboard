from django.db import models


class LeanBand(models.Model):
    _Id = models.AutoField(primary_key=True)
    lbname = models.IntegerField(default=None)


class ModuleTarget(models.Model):
    _Id = models.AutoField(primary_key=True)
    lb_Id = models.ForeignKey(LeanBand, on_delete=models.CASCADE, default=None)
    TDate = models.DateField()
    Shift = models.CharField(max_length=2)
    HeadCount = models.IntegerField()


class DowntimeCode(models.Model):
    _id = models.AutoField(primary_key=True)
    DTCode = models.CharField(max_length=10, null=False)
    Department = models.CharField(max_length=10, null=False)


class HeadsTarget(models.Model):
    _Id = models.AutoField(primary_key=True)
    module_id = models.ForeignKey(ModuleTarget, on_delete=models.CASCADE)

    HeadNumber = models.IntegerField(null=True)
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


class HeadDowntime(models.Model):
    _id = models.AutoField(primary_key=True)
    Head_id = models.ForeignKey(HeadsTarget, on_delete=models.CASCADE)
    StartTime = models.TimeField(null=False)
    EndTime = models.TimeField(null=False)
    DTCode = models.ForeignKey(DowntimeCode, on_delete=models.CASCADE)
    Status = models.CharField(max_length=10, default=None)
