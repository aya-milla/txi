# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labworks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='condition',
            field=models.CharField(choices=[('checked', 'Проверена'), ('not checked', 'Не проверена')], default='not checked', max_length=50),
        ),
        migrations.AlterField(
            model_name='lab',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='lab',
            name='mark',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]