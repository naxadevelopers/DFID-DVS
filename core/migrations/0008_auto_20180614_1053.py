# Generated by Django 2.0.4 on 2018-06-14 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180614_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_program', to='core.Program'),
        ),
    ]