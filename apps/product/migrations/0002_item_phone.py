# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name='User ID')),
                ('status', models.SmallIntegerField(verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, '\u041d\u0435 \u043f\u0440\u043e\u0434\u0430\u043d\u043e'), (1, '\u041f\u0440\u043e\u0434\u0430\u043d\u043e')])),
            ],
            options={
                'verbose_name': '\u0412\u0435\u0449\u044c',
                'verbose_name_plural': '\u0412\u0435\u0449\u0438',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=128, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('user', models.IntegerField(verbose_name='User ID')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d',
                'verbose_name_plural': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b',
            },
        ),
    ]
