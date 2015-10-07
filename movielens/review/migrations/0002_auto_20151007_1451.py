# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(default='neutral', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.CharField(default='n/a occ', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
