# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imartl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imartl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('librarian_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='librarian',
            name='user',
        ),
        migrations.DeleteModel(
            name='Librarian',
        ),
    ]
