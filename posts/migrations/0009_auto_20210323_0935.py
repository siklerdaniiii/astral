# Generated by Django 3.1.5 on 2021-03-23 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210321_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owners_posts', to='posts.postowner'),
        ),
    ]
