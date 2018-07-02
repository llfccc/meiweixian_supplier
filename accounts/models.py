# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chinese_name = models.CharField(max_length=100, unique=True,verbose_name='姓名',blank=True, null=True)
    company_name = models.CharField(max_length=100, verbose_name='公司名称')
    process_company = models.CharField(max_length=100, verbose_name='正在处理的公司',blank=True, null=True)

    def __unicode__(self):
        return self.chinese_name
