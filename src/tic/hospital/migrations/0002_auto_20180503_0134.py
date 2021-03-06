# Generated by Django 2.0.1 on 2018-05-03 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('is_reserved', models.BooleanField(default=False)),
                ('is_purchased', models.BooleanField(default=False)),
                ('reserve_deadline', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.HospitalEvent')),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='hopitalticket',
            name='owner',
        ),
        migrations.DeleteModel(
            name='HopitalTicket',
        ),
    ]
