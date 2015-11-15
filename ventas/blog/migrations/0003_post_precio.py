# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151030_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0),
        ),
    ]
