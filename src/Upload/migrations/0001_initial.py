# Generated by Django 2.2.3 on 2019-07-25 08:58

import datetime
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnoTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=64)),
                ('size', django.contrib.postgres.fields.jsonb.JSONField()),
                ('format', django.contrib.postgres.fields.jsonb.JSONField()),
                ('project_scene', models.CharField(max_length=32)),
                ('project_type', models.CharField(max_length=32)),
                ('project', models.CharField(max_length=32)),
                ('ano_type', models.CharField(default='pascal_voc', max_length=16)),
                ('ano', django.contrib.postgres.fields.jsonb.JSONField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, size=None)),
                ('time_add', models.DateField(default=datetime.date(2019, 7, 25))),
                ('check', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'annotation_test',
            },
        ),
    ]