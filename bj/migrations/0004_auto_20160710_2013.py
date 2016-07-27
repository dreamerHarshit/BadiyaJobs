# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bj', '0003_auto_20160710_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_english',
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
                ('role_id', models.ForeignKey(to='bj.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Job_hindi',
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
                ('role_id', models.ForeignKey(to='bj.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Job_hinglish',
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
                ('role_id', models.ForeignKey(to='bj.Role')),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='job',
            name='role_id',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
