# Generated by Django 2.0.4 on 2018-08-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20180803_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=200, verbose_name='NAME'),
        ),
    ]
