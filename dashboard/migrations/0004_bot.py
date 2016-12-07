# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_gputype_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100, unique=True, verbose_name='Bot Password')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Bot Name')),
                ('cpuDetail', models.CharField(blank=True, max_length=100, verbose_name='CPU Details')),
                ('gpuDetail', models.CharField(blank=True, max_length=100, verbose_name='CPU Details')),
                ('platformDetail', models.CharField(blank=True, max_length=100, verbose_name='CPU Details')),
                ('enabled', models.BooleanField(default=False)),
                ('cpuArchitecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.CPUArchitecture')),
                ('gpuType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.GPUType')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Platform')),
            ],
        ),
    ]