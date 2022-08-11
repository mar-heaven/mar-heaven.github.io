---
title: django 图片储存七牛云
date: 2019-11-27 02:01:47
author: Ginta
img: http://img.ginta.top/lc3.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/lc3.jpg
toc: false
mathjax: false
summary:
tags: 
  - python
  - Django
categories: python
---
## 前言
每次给博客添加一篇文章的时候，上传图片的时候总要心痛一下，因为服务器的空间很有限，最主要的还是感觉把博客的图片和代码放到一个地方总有种污染代码的感觉，以前就听说了七牛云很方便，于是就用一下了。

## 开始
首先我们要新建一个七牛云的储存空间，具体操作如下。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191115112528531.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)
进入这里，点击 **对象存储**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191115112615815.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)
**新建存储空间** ，存储空间的名称随意就好，配置可以仿照这里图片这个样子，然后就OK了，对于新用户首先要实名认证，不过挺快的，我申请了2个小时不到就通过了。

## 使用
- 首先安装依赖包
`pip install django-qiniu-storage`
- 然后 **settings.py** 配置新增如下
```python
# 七牛云配置

QINIU_ACCESS_KEY = 'ACCESS_KEY'
# 七牛给开发者分配的AccessKey
QINIU_SECRET_KEY = 'SECRET_KEY'
# 七牛给开发者分配的Secret
QINIU_BUCKET_NAME = 'myblog'  # 就是刚才新建的存储空间名称
# 用来存放文件的七牛空间(bucket)的名字
QINIU_BUCKET_DOMAIN = '*****.bkt.clouddn.com/'
# 七牛空间(bucket)的域名，别遗漏了后面的/
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'
# 只用七牛托管动态生成的文件（例如用户上传的文件）
QINIU_SECURE_URL = False
# 使用http

PREFIX_URL = 'http://'
# 文件系统更改
MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN
MEDIA_ROOT = 'media/'
```
**QINIU_BUCKET_DOMAIN** 的位置如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191115113248223.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)

我的轮播图 *model* 如下
```python
class Banner(BaseModel):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    """
    轮播图
    """
    # upload_to 存储子目录，真实存放地址会使用配置中的MADIE_ROOT+upload_to
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True,
                              blank=True, help_text="轮播图片的大小规格：1920x720，或者对应的比例的图片")
    name = models.CharField(max_length=150, verbose_name='轮播图名称')
    desc = models.CharField(max_length=250, verbose_name='描述信息', help_text="请填写描述信息")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='状态')
    link = models.CharField(max_length=150, verbose_name='轮播图广告地址')

    class Meta:
        db_table = 'home_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
```
注意 **image** 这个字段，我设置了 `upload_to='banner'` ，他就会保存到  **MADIE_ROOT+'banner'** 这个路径下，而 **MADIE_ROOT** 在配置中是 `MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN` ,也就是 `'http://*****.bkt.clouddn.com/'`
于是我们的轮播图图片就会保存到类似这样的url下：
`http://*****.bkt.clouddn.com/banner/20160923084104779_jAQ76Kw.jpg`

## 总结
基本操作就是这样了，因为网上有很多大佬已经踩过坑了，所以避免了不少麻烦。**七牛云不止可以存储图片，也可以存储其他文件，CDN加速等等，以后有需要会补充上的。**