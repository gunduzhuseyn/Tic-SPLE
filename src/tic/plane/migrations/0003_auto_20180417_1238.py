# Generated by Django 2.0.1 on 2018-04-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0002_auto_20180417_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='planeevent',
            name='flight_number',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='planeevent',
            name='location_to',
            field=models.CharField(default='', max_length=500),
        ),
    ]