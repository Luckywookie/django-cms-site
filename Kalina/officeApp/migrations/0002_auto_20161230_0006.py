# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('officeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, related_name='officeapp_officelink', parent_link=True, serialize=False, primary_key=True, to='cms.CMSPlugin')),
                ('office', models.ForeignKey(verbose_name='Office', to='officeApp.OfficeItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='officelinks',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='officelinks',
            name='office',
        ),
        migrations.DeleteModel(
            name='OfficeLinks',
        ),
    ]
