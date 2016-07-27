# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comany_name', models.CharField(max_length=70)),
                ('year_founded', models.IntegerField(max_length=70)),
                ('no_of_employee', models.CharField(max_length=80)),
                ('about', models.CharField(max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comany_name', models.CharField(max_length=70)),
                ('job_role', models.CharField(max_length=100)),
                ('in_hand_salary', models.IntegerField()),
                ('location', models.CharField(max_length=70)),
                ('i', models.CharField(max_length=70)),
                ('salary_detail', models.IntegerField()),
                ('job_type', models.CharField(max_length=70)),
                ('shift', models.CharField(max_length=70)),
                ('timings', models.CharField(max_length=70)),
                ('education_requried', models.CharField(max_length=70)),
                ('min_work_exp', models.CharField(max_length=70)),
                ('job_description', models.CharField(max_length=500)),
                ('accomodation', models.CharField(max_length=70)),
                ('food', models.CharField(max_length=70)),
                ('company_id', models.ForeignKey(to='bj.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=70)),
                ('about', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='role_id',
            field=models.ForeignKey(to='bj.Roles'),
        ),
    ]
