# Generated by Django 2.2.1 on 2019-10-11 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplemodel',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examplemodel',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
