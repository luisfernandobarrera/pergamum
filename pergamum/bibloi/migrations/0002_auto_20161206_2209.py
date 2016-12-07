# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('bibloi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.CharField(choices=[('POLIT', 'Politician'), ('PERIO', 'Journalist')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
