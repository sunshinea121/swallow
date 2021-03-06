# Generated by Django 2.1 on 2019-04-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(help_text='供应商名称', max_length=64, unique=True, verbose_name='供应商名称')),
                ('phone', models.CharField(blank=True, help_text='电话', max_length=16, null=True, verbose_name='电话')),
                ('remark', models.TextField(blank=True, help_text='备注', max_length=255, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
                'ordering': ['id'],
            },
        ),
    ]
