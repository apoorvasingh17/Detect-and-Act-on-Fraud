# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 06:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CARDDETAILS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('cardnumber', models.CharField(max_length=20)),
                ('mm', models.IntegerField()),
                ('yy', models.IntegerField()),
                ('cvv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('USER_REF', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='USER', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('NAME', models.CharField(max_length=100)),
                ('PROFILE_LINK', models.CharField(max_length=100)),
                ('EXPERIENCE_UPVOTE', models.IntegerField()),
                ('ANSWER_UPVOTE', models.IntegerField()),
                ('GUIDE_UPVOTE', models.IntegerField()),
                ('NUM_QUESTION_ASKED', models.IntegerField()),
                ('BADGE1', models.BooleanField(default=False)),
                ('BADGE2', models.BooleanField(default=False)),
                ('BADGE3', models.BooleanField(default=False)),
                ('BADGE4', models.BooleanField(default=False)),
                ('BADGE5', models.BooleanField(default=False)),
            ],
        ),
    ]
