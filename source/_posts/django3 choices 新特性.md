---
title: django3 choices 新特性
date: 2019-12-04 03:43:14
author: Ginta
img: http://img.ginta.top/chaoshou1.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/chaoshou1.jpg
toc: false
mathjax: false
summary:
tags: 
  - django3
categories: Django
---
## 前言
等了好久的 **Django3** 正式版本终于发布了！在看官方文档的时候看到有这么一句
>
Custom enumeration types TextChoices, IntegerChoices, and Choices are now available as a way to define Field.choices. TextChoices and IntegerChoices types are provided for text and integer fields

具体是什么意思呢，解释起来比较麻烦，还是上代码比较清晰：
```
from django.db import models

# Create your models here.

class Student(models.Model):

    class Gender(models.IntegerChoices):
        MALE = 1
        FEMALE = 2

    gender = models.IntegerField(choices=Gender.choices)
```
这里新建了一个学生模型，里面只有一个性别字段。如果是以前的写法应该是这样：
```
from django.db import models

# Create your models here.

class Student(models.Model):

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(choices=gender_choices)
```
直接看起来好像并没有方便多少，只是在内部新建了一个类而已，确实如此，不过还是有区别的，比如这里我们要求字段的值是 **整数** ，新的写法会自动进行类型检查：
```
class Student(models.Model):

    class Gender(models.IntegerChoices):
        MALE = "ga", gettext_lazy('男')
        FEMALE = 2, gettext_lazy('女')

    gender = models.IntegerField(choices=Gender.choices)
```
如果我们这样写，**MALE** 的值改为 "ga"，在执行 `python manage.py makemigrations` 的时候会抛出以下错误：
>
ValueError: invalid literal for int() with base 10: 'ga'

如果是以前的代码则不会报错。


![](http://img.ginta.top/markdownx/2019/12/02/2623de9b-3a47-4bca-bed4-3329a738c558.png)
这是后台显示，如果想显示中文也是可以的，把代码改成如下
```
from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.


class Student(models.Model):

    class Gender(models.IntegerChoices):
        MALE = 1, gettext_lazy('男')
        FEMALE = 2, gettext_lazy('女')

    gender = models.IntegerField(choices=Gender.choices)

```



![](http://img.ginta.top/markdownx/2019/12/02/dfa2606d-27a6-4463-822a-8b21fec49121.png)

这就是效果了。如果是要求值是字符串，同理，只不过继承的类就不是 **models.IntegerChoices** ， 而是 **models.TextChoices** 。