# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bj', '0002_auto_20160710_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
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
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='role_id',
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
        migrations.AddField(
            model_name='job',
            name='role_id',
            field=models.ForeignKey(to='bj.Role'),
        ),
    ]
