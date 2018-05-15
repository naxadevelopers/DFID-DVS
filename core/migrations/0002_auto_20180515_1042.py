# Generated by Django 2.0.4 on 2018-05-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='layerdata',
            name='layer_path',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='layerdata',
            name='layer_server_url',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='layerdata',
            name='file',
            field=models.FileField(null=True, upload_to='layer/'),
        ),
    ]
