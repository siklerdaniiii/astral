# Generated by Django 3.1.5 on 2021-03-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210323_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_mobile_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
