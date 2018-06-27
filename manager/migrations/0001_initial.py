# Generated by Django 2.0.6 on 2018-06-27 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('combat_type', models.IntegerField(default=0)),
                ('power', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear_level', models.IntegerField(default=0)),
                ('power', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('rarity', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Character')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('player_id', models.CharField(max_length=30)),
                ('ally_code', models.CharField(max_length=11)),
                ('player_name', models.CharField(max_length=100)),
                ('swgoh_name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.User'),
        ),
    ]