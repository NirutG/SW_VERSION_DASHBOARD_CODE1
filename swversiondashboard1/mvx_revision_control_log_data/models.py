from django.db import models

# Create your models here.
class InlineActualVersion(models.Model):
    line = models.CharField(max_length=35, default='', null=True)

    exe_0950_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_0950_actual_status = models.CharField(max_length=35, default='', null=True)
    plc_0950_actual_version = models.CharField(max_length=35, default='', null=True)
    plc_0950_actual_status = models.CharField(max_length=35, default='', null=True)
    hmi_0950_actual_version = models.CharField(max_length=35, default='', null=True)
    hmi_0950_actual_status = models.CharField(max_length=35, default='', null=True)

    exe_1560_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_1560_actual_status = models.CharField(max_length=35, default='', null=True)

    plc_1580_actual_version = models.CharField(max_length=35, default='', null=True)
    plc_1580_actual_status = models.CharField(max_length=35, default='', null=True)
    hmi_1580_actual_version = models.CharField(max_length=35, default='', null=True)
    hmi_1580_actual_status = models.CharField(max_length=35, default='', null=True)

    plc_1586_actual_version = models.CharField(max_length=35, default='', null=True)
    plc_1586_actual_status = models.CharField(max_length=35, default='', null=True)
    hmi_1586_actual_version = models.CharField(max_length=35, default='', null=True)
    hmi_1586_actual_status = models.CharField(max_length=35, default='', null=True)

    exe_1587_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_1587_actual_status = models.CharField(max_length=35, default='', null=True)
    plc_1587_actual_version = models.CharField(max_length=35, default='', null=True)
    plc_1587_actual_status = models.CharField(max_length=35, default='', null=True)
    hmi_1587_actual_version = models.CharField(max_length=35, default='', null=True)
    hmi_1587_actual_status = models.CharField(max_length=35, default='', null=True)

    exe_1595_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_1595_actual_status = models.CharField(max_length=35, default='', null=True)

    exe_1596_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_1596_actual_status = models.CharField(max_length=35, default='', null=True)

    exe_1750_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_1750_actual_status = models.CharField(max_length=35, default='', null=True)

    
class OfflineActualVersion(models.Model):
    line = models.CharField(max_length=35, default='', null=True)

    exe_1600_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_1600_actual_status = models.CharField(max_length=35, default='', null=True)
    
    exe_1700_actual_version = models.CharField(max_length=35, default='', null=True)
    exe_1700_actual_status = models.CharField(max_length=35, default='', null=True)