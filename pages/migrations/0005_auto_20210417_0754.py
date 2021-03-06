# Generated by Django 3.1.7 on 2021-04-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210412_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_unique_field',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_slug',
            field=models.CharField(choices=[('home_1', 'Kezdőlap #1'), ('home_2', 'Kezdőlap #2'), ('home_3', 'Kezdőlap #3'), ('home_4', 'Kezdőlap #4'), ('home_5', 'Kezdőlap #5'), ('about', 'Rólam'), ('gdpr', 'Adatkezelési nyilatkozat'), ('aszf', 'Általános szerődési feltételek')], max_length=254, unique=True),
        ),
    ]
