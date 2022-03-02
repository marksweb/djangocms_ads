# Generated by Django 3.2.12 on 2022-02-28 23:34

from __future__ import annotations

import django.db.models.deletion
from django.db import migrations, models

import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0034_remove_pagecontent_placeholders'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdSlotPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_ads_adslotplugin', serialize=False, to='cms.cmsplugin')),
                ('internal_name', models.CharField(help_text='Provide internal name for Ad slot.', max_length=255, verbose_name='internal name')),
                ('ad_unit_path', models.CharField(help_text="The first item provided by google for the slot, e.g. '/4321234/MPU'", max_length=255, verbose_name='Ad unit path')),
                ('sizes', models.CharField(help_text='The second item provided by google for the slot, e.g. [300, 250]', max_length=255, verbose_name='Ad sizes')),
                ('div_id', models.CharField(help_text="The third item provided by google for the slot, e.g. 'div-gpt-ad-12345-0'", max_length=100, verbose_name='Div ID')),
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
            options={
                'verbose_name': 'ad slot',
                'verbose_name_plural': 'ad slots',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AdvancedAdContainerPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_ads_advancedadcontainerplugin', serialize=False, to='cms.cmsplugin')),
                ('internal_name', models.CharField(help_text='Provide internal name for Ad slot.', max_length=255, verbose_name='internal name')),
                ('content', models.TextField(help_text='The script tag for the head of the page', verbose_name='Advert script tag')),
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
            options={
                'verbose_name': 'Advanced ad container',
                'verbose_name_plural': 'Advanced ad containers',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AdvertPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_ads_advertplugin', serialize=False, to='cms.cmsplugin')),
                ('label', models.CharField(max_length=120, verbose_name='label')),
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('div_id', models.CharField(help_text="The third item provided by google for the slot, e.g. 'div-gpt-ad-12345-0'", max_length=100, verbose_name='Div ID')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'verbose_name': 'advert plugin model',
                'verbose_name_plural': 'advert plugin models',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SimpleAdContainerPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_ads_simpleadcontainerplugin', serialize=False, to='cms.cmsplugin')),
                ('internal_name', models.CharField(help_text='Provide internal name for Ad slot.', max_length=255, verbose_name='internal name')),
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
            options={
                'verbose_name': 'Simple ad container',
                'verbose_name_plural': 'Simple ad containers',
            },
            bases=('cms.cmsplugin',),
        ),
    ]