# Generated by Django 4.2.8 on 2023-12-12 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Vdetection', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='upload_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
