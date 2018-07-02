# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Invoices(models.Model):
    supplier = models.TextField()
    add_date = models.DateTimeField(blank=True, null=True)
    order_code = models.TextField()
    storage_code = models.TextField()
    stock_code = models.TextField()
    material_name = models.TextField()
    brand = models.TextField(blank=True, null=True)
    serial_number = models.TextField(blank=True, null=True)
    model = models.TextField()
    unit = models.TextField()
    number = models.FloatField()
    notaxprice = models.FloatField(db_column='noTaxPrice')  # Field name made lowercase.
    notaxmoney = models.FloatField(db_column='noTaxMoney')  # Field name made lowercase.
    price = models.FloatField()
    stagequotation = models.TextField(db_column='stageQuotation')  # Field name made lowercase.
    timestamp = models.DateField()
    settledate = models.DateTimeField(db_column='settleDate', blank=True, null=True)  # Field name made lowercase.
    current_company = models.CharField(max_length=512)




class U8S(models.Model):
    add_date = models.DateTimeField(blank=True, null=True,verbose_name="订单日期")
    supplier = models.CharField(max_length=64, blank=True, null=True,verbose_name="供应商")
    up_code = models.IntegerField(blank=True, null=True,verbose_name="请购单号")
    order_code = models.IntegerField(blank=True, null=True,verbose_name="订单号")
    stock_code = models.CharField(max_length=64, blank=True, null=True,verbose_name="存货编码")
    material_name = models.CharField(max_length=64, blank=True, null=True,verbose_name="物资名称")
    brand = models.CharField(max_length=512, blank=True, null=True,verbose_name="品牌")
    serial_number = models.CharField(max_length=512, blank=True, null=True,verbose_name="货号")
    model = models.CharField(max_length=64, blank=True, null=True,verbose_name="型号")
    unit = models.CharField(max_length=64, blank=True, null=True,verbose_name="单位")
    number = models.FloatField(blank=True, null=True,verbose_name="数量")
    price = models.FloatField(blank=True, null=True,verbose_name="价格")
    received = models.IntegerField(blank=True, null=True,verbose_name="是否接收")
    deliver_date = models.DateTimeField(blank=True, null=True,verbose_name="预计送货日期")
    remarks = models.CharField(max_length=512, blank=True, null=True,verbose_name="供应商备注")
    comment1 = models.TextField(verbose_name="备注1")
    arrival_date = models.DateTimeField(blank=True, null=True,verbose_name="送货日期")
    current_company = models.CharField(max_length=512,verbose_name="所属公司")
    timestamp = models.DateTimeField(blank=True, null=True)

 