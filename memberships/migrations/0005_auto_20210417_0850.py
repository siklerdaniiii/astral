# Generated by Django 3.1.7 on 2021-04-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_auto_20210417_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_name',
        ),
        migrations.AlterField(
            model_name='member',
            name='member_status',
            field=models.IntegerField(choices=[(0, 'Nem aktív'), (1, 'Aktív')], default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan_status',
            field=models.IntegerField(choices=[(0, 'Vázlat'), (1, 'Őublikálva')], default=0),
        ),
    ]
