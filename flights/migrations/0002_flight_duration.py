# Generated by Django 5.0.6 on 2024-05-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='duration',
            field=models.IntegerField(default=360),
        ),
    ]
