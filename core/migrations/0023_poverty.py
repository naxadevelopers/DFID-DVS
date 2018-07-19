# Generated by Django 2.0.4 on 2018-07-19 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_area_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poverty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lgu', models.CharField(max_length=250)),
                ('lu_type', models.CharField(max_length=250)),
                ('lgu_FGT_0', models.FloatField()),
                ('lgu_FGT_1', models.FloatField()),
                ('lgu_FGT_2', models.FloatField()),
                ('female_lit_rate', models.FloatField()),
                ('male_lit_rate', models.FloatField()),
                ('total_lit_rate', models.FloatField()),
                ('hlcit_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Area')),
            ],
        ),
    ]
