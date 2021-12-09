# Generated by Django 3.2.9 on 2021-12-09 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InlineActualVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(default='', max_length=35, null=True)),
                ('exe_0950_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_0950_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('plc_0950_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('plc_0950_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('hmi_0950_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('hmi_0950_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('exe_1560_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_1560_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('plc_1580_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('plc_1580_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('hmi_1580_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('hmi_1580_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('plc_1586_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('plc_1586_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('hmi_1586_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('hmi_1586_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('exe_1587_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_1587_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('plc_1587_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('plc_1587_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('hmi_1587_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('hmi_1587_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('exe_1595_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_1595_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('exe_1596_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_1596_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('exe_1750_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_1750_actual_status', models.CharField(default='', max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfflineActualVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(default='', max_length=35, null=True)),
                ('exe_1600_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_1600_actual_status', models.CharField(default='', max_length=35, null=True)),
                ('exe_1700_actual_version', models.CharField(default='', max_length=35, null=True)),
                ('exe_1700_actual_status', models.CharField(default='', max_length=35, null=True)),
            ],
        ),
    ]
