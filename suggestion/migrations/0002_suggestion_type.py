# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='type',
            field=models.CharField(default='fuckin_round', max_length=200),
            preserve_default=False,
        ),
    ]
