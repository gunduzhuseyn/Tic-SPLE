# Generated by Django 2.0.1 on 2018-04-23 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('plane', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planeevent',
            name='schedule',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.Schedule'),
        ),
        migrations.AddField(
            model_name='planeticket',
            name='schedule',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.Schedule'),
        ),
    ]