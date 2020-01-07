from django.db import models

# Create your models here.

class Product(models.Model):
    productName =models.CharField('产品名称', max_length=64) #产品名称
    productDesc=models.CharField('产品描述',max_length=200)
    producter=models.CharField('产品负责人',max_length=200)
    create_time=models.DateField('创建时间',auto_now=True)

    def __str__(self):
        return self.productName
