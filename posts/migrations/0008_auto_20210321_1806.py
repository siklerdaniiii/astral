# Generated by Django 3.1.5 on 2021-03-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210321_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
