# Generated by Django 2.0.8 on 2018-11-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0022_auto_20181103_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='image',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='guild',
            name='total_power',
            field=models.IntegerField(default=0),
        ),
    ]
