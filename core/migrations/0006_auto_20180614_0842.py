# Generated by Django 2.0.4 on 2018-06-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='hlcit_code',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='programs',
            field=models.ManyToManyField(blank=True, to='core.Program'),
        ),
    ]
