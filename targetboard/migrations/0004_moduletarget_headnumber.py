# Generated by Django 4.0.2 on 2022-03-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetboard', '0003_rename_ddate_downtime_dtdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moduletarget',
            name='HeadNumber',
            field=models.IntegerField(null=True),
        ),
    ]
