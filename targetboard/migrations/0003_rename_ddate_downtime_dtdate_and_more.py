# Generated by Django 4.0.2 on 2022-03-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetboard', '0002_rename_planhour_moduletarget_planh_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downtime',
            old_name='DDate',
            new_name='DTDate',
        ),
        migrations.RenameField(
            model_name='moduletarget',
            old_name='MAID',
            new_name='HeadID',
        ),
        migrations.RenameField(
            model_name='moduletarget',
            old_name='HeadNo',
            new_name='hour10re',
        ),
        migrations.RenameField(
            model_name='moduletarget',
            old_name='PlanH',
            new_name='planhour',
        ),
        migrations.RenameField(
            model_name='moduletarget',
            old_name='PotentialH',
            new_name='potenetialhour',
        ),
        migrations.RemoveField(
            model_name='downtime',
            name='DAID',
        ),
        migrations.RemoveField(
            model_name='downtime',
            name='LBId',
        ),
        migrations.AddField(
            model_name='downtime',
            name='DTId',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='downtime',
            name='LBID',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour11re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour12re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour1re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour2re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour3re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour4re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour5re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour6re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour7re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour8re',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moduletarget',
            name='hour9re',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='downtime',
            name='HeadNo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='downtime',
            name='Shift',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='LBId',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='Shift',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour10',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour11',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour12',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour6',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour7',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour8',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='moduletarget',
            name='hour9',
            field=models.IntegerField(null=True),
        ),
    ]