# Generated by Django 2.0.4 on 2018-08-28 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20180805_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramSpendAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hlcit_code', models.CharField(max_length=300, unique=True)),
                ('local_unit', models.CharField(max_length=300)),
                ('partneship', models.CharField(max_length=300)),
                ('spend_allocation_npr', models.FloatField()),
                ('spend_allocation_gbp', models.FloatField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_spend_allocation', to='core.District')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_spend_allocation', to='core.Program')),
            ],
        ),
    ]
