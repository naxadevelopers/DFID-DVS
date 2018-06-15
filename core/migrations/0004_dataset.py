# Generated by Django 2.0.4 on 2018-06-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180516_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('source', models.TextField()),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
    ]
