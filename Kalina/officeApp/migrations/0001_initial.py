# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True, parent_link=True, related_name='officeapp_officeitem')),
                ('number', models.CharField(max_length=36, verbose_name='Номер офиса')),
                ('floor', models.PositiveIntegerField(default=0, verbose_name='Этаж')),
                ('metres', models.PositiveIntegerField(default=0, verbose_name='Количество метров')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('desc', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='offices', blank=True)),
                ('is_free', models.BooleanField(default=False, verbose_name='Свободен')),
                ('published', models.BooleanField(default=False, verbose_name='Публикация')),
            ],
            options={
                'ordering': ['-number', 'floor'],
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='OfficeLinks',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True, parent_link=True, related_name='officeapp_officelinks')),
                ('office', models.ForeignKey(to='officeApp.OfficeItem', verbose_name='Office')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
