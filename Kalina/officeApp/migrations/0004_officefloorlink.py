# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('officeApp', '0003_auto_20161230_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeFloorLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, related_name='officeapp_officefloorlink', auto_created=True, primary_key=True, parent_link=True, to='cms.CMSPlugin')),
                ('office', models.ForeignKey(to='officeApp.OfficeItem', verbose_name='Office')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
