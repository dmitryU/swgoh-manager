# Generated by Django 2.0.6 on 2018-07-23 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0019_playerstats'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerStats',
            new_name='PlayerStat',
        ),
        migrations.AlterUniqueTogether(
            name='playerstat',
            unique_together={('player', 'week')},
        ),
    ]