# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 11:02
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '__latest__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodytext', models.TextField(verbose_name='message')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', verbose_name='ip address')),
                ('user_name', models.CharField(default='anonymous', max_length=50, verbose_name='user name')),
                ('user_email', models.EmailField(blank=True, max_length=254, verbose_name='user email')),
            ],
            options={
                'ordering': ['post_date'],
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField()),
                ('bodytext', models.TextField(verbose_name='message')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('modified', models.DateTimeField(null=True, verbose_name='modified')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('comment_count', models.IntegerField(blank=True, default=0, verbose_name='comment count')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='posted by')),
            ],
            options={
                'ordering': ['-post_date'],
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='simpleblog.Post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
