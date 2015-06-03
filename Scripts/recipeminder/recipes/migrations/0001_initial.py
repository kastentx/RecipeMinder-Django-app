# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True)),
                ('servings', models.PositiveIntegerField(null=True)),
                ('ingredients', models.TextField(null=True)),
                ('instructions', models.TextField(null=True)),
            ],
        ),
    ]
