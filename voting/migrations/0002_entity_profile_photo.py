# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='profile_photo',
            field=models.ImageField(default='defaultProfilePhoto.jpg', max_length=200, null=True, upload_to='profilePhoto/'),
        ),
    ]
