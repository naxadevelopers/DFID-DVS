# Generated by Django 2.0.4 on 2018-08-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]