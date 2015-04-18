# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AQI', models.IntegerField()),
                ('pm25', models.IntegerField()),
                ('pm10', models.IntegerField()),
                ('CO', models.FloatField()),
                ('NO2', models.IntegerField()),
                ('O31', models.IntegerField()),
                ('O38', models.IntegerField()),
                ('SO2', models.IntegerField()),
                ('date', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pollution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pollution', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='data',
            name='grade',
            field=models.ForeignKey(to='pmdata.Grade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='pollution',
            field=models.ForeignKey(to='pmdata.Pollution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='sid',
            field=models.ForeignKey(to='pmdata.Place'),
            preserve_default=True,
        ),
    ]
