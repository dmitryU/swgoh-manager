# Generated by Django 2.0.6 on 2018-06-27 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_character_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Player',
        ),
    ]
