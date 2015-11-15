# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='precio',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='fecha_de_creacion',
            new_name='fecha_creacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='producto',
            new_name='titulo',
        ),
    ]
