# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('team_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('home_city', models.CharField(max_length=20)),
                ('rank', models.IntegerField()),
                ('conference', models.CharField(choices=[('EAST', 'EASTERN'), ('WEST', 'WESTERN')], default=None, max_length=4)),
                ('num_wins', models.IntegerField()),
                ('num_losses', models.IntegerField()),
            ],
        ),
    ]
