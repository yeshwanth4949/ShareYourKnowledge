# Generated by Django 3.1.7 on 2021-05-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(default='NotAccepted', max_length=100),
        ),
    ]
