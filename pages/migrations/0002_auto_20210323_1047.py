# Generated by Django 3.1.5 on 2021-03-23 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=200, unique=True)),
                ('paget_description', models.TextField()),
                ('page_image', models.ImageField(default='pages/default.jpg', upload_to='pages')),
                ('page_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('page_mobile_id', models.CharField(blank=True, max_length=200, null=True)),
                ('page_updated_at', models.DateTimeField(auto_now=True)),
                ('page_created_at', models.DateTimeField(auto_now_add=True)),
                ('page_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authors_pages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-page_created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
