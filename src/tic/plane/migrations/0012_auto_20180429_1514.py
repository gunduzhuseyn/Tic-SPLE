# Generated by Django 2.0.1 on 2018-04-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0011_auto_20180429_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='is_empty',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_no',
            field=models.IntegerField(default=0),
        ),
    ]
