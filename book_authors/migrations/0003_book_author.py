# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-14 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='book_authors.Author'),
        ),
    ]
