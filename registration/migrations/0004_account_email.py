# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20141001_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=75, unique=True, default=datetime.date(2014, 10, 1)),
            preserve_default=False,
        ),
    ]
