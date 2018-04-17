# Generated by Django 2.0.1 on 2018-04-17 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatingplan',
            name='plane_event',
        ),
        migrations.AddField(
            model_name='planeevent',
            name='seating_plan',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='plane.SeatingPlan'),
        ),
    ]
