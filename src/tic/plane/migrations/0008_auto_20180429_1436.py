# Generated by Django 2.0.1 on 2018-04-29 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0007_auto_20180429_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planeticket',
            old_name='plane_event',
            new_name='event',
        ),
    ]
