# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibloi', '0006_article_source_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='source_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
