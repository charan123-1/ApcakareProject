# Generated by Django 3.1.7 on 2021-06-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210630_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excel',
            name='District',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='GA',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='GO',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='GT',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='IBAvailable',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='IBOccupied',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='IBTotal',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='O2A',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='O2O',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='O2T',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='SNO',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='VA',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='VO',
        ),
        migrations.RemoveField(
            model_name='excel',
            name='VT',
        ),
        migrations.AddField(
            model_name='excel',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='excel',
            name='userid',
            field=models.CharField(default='charan', max_length=30),
        ),
    ]
