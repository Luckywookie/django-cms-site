# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeApp', '0002_auto_20161230_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officelink',
            old_name='office',
            new_name='news',
        ),
    ]
