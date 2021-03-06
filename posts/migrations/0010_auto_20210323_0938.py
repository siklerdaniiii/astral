# Generated by Django 3.1.5 on 2021-03-23 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210323_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_posts', to='posts.postcategory'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owners_posts', to='posts.postowner'),
        ),
    ]
