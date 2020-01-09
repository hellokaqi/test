from django.db import models
from product.models import Product

# Create your models here.

class Test(models.Model):
    name=models.CharField(max_length=20)


class Apitest(models.Model):
    Product=models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    apitestname=models.CharField('流程接口名称',max_length=64) #接口名称
    apitestdesc=models.CharField('描述',max_length=64,null=True) #接口描述
    apitester=models.CharField('执行人',max_length=16) #执行人
    apitestresult=models.BooleanField('执行结果')
    creat_time=models.DateField('创建时间',auto_now=True)

    class Meta:
        verbose_name='流程接口'

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    Apitest=models.ForeignKey(Apitest,on_delete=models.CASCADE)
    #接口标题
    apiname=models.CharField('接口名称',max_length=100)
    #地址
    apiurl=models.CharField('url地址',max_length=100)
    #测试步骤
    apistep=models.CharField('测试步骤',max_length=800)
    #参数和值
    apiparamvalue=models.CharField('参数',max_length=800)
    #请求方法
    REQUEST_METHOD=(('get','get'),('post','post'),('put','put'),('delete','delete'))
    apimethod=models.CharField(verbose_name='请求方法',choices=REQUEST_METHOD,default='get',max_length=200,null=True)

    #预期结果
    apiresult=models.CharField('预期结果',max_length=800)
    #响应数据
    apiresponse=models.CharField('响应数据',max_length=800)
    #测试结果
    apistatus=models.BooleanField('是否通过')
    #创建时间
    create_time=models.DateField('创建时间',auto_now=True)

    def __str__(self):
        return self.name
    



