# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
                ('occupation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('rating', models.IntegerField()),
                ('movie_id', models.ForeignKey(to='review.Movie')),
                ('rater_id', models.ForeignKey(to='review.Rater')),
            ],
        ),
    ]
