# Generated by Django 2.0.1 on 2018-04-29 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0005_auto_20180429_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='planeticket',
            name='seat',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='plane.Seat'),
        ),
    ]
