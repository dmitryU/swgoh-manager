# Generated by Django 2.0.6 on 2018-07-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_player_total_useful'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='total_chars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_power',
            field=models.IntegerField(default=0),
        ),
    ]
