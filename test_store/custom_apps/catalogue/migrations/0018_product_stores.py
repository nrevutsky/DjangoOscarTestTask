# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_store_store_admins'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stores',
            field=models.ManyToManyField(through='catalogue.StoreProduct', to='catalogue.Store', verbose_name='Store'),
        ),
    ]
