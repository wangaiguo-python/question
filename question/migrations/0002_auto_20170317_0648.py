# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': '答案', 'verbose_name': '答案'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '分类', 'verbose_name': '分类'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': '问题', 'verbose_name': '问题'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(help_text='勾选为正确答案', verbose_name='正确答案'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(help_text='简单描述,可填可不填', null=True, verbose_name='描述', blank=True),
        ),
    ]
