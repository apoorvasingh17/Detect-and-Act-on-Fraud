# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FraudDetection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=5)),
                ('product_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
