# Generated by Django 2.0.4 on 2018-06-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_pdf_province'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='program',
        ),
        migrations.AddField(
            model_name='partner',
            name='program',
            field=models.ManyToManyField(null=True, related_name='partner_program', to='core.ProgramData'),
        ),
    ]