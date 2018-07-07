# Generated by Django 2.0.6 on 2018-07-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20180706_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='combat_type',
            field=models.IntegerField(choices=[(1, 'character'), (2, 'ship')], default=1),
        ),
    ]
