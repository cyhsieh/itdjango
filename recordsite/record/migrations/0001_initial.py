# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('content', models.CharField(max_length=30)),
                ('duration', models.DecimalField(max_digits=3, decimal_places=0, blank=True)),
                ('note', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='subject',
            field=models.ForeignKey(to='record.Subject'),
        ),
    ]
