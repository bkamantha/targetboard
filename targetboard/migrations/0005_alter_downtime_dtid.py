# Generated by Django 4.0.2 on 2022-03-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetboard', '0004_moduletarget_headnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downtime',
            name='DTId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
