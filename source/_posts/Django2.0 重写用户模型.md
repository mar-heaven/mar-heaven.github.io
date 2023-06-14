---
title: Django2.0 重写用户模型
date: 2019-11-27 03:00:59
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
categories: Django
published: false
---
前言

现有的 django 自带的用户模型已经不满足我们的需求了，比如用户有头像以及性别等字段，于是乎我们需要自定义一个新的用户模型，但是有一部分字段还是可以用以前的，比如邮箱什么的，所以采用继承关系就好。



步骤

重写用户模型，继承 django.contrib.auth.models.AbstractUser 类

```

# users.py

from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    mobiles = models.CharField(verbose_name="手机号码", max_length=15, unique=True)

    avatar = models.ImageField(upload_to='avatar', verbose_name='头像', null=True,

                               blank=True, help_text="头像图片的大小规格：256*256，或者对应的比例的图片")



    class Meta:

        db_table = 'blog_users'

        verbose_name = '用户'

        verbose_name_plural = verbose_name

```

在 settings.py 中更改用户认证模型的指向



```

# settings.py

# ...其他代码

# 配置让Django的Auth模块调用users子应用下的User模型

AUTH_USER_MODEL = "users.User"

# ...其他代码

```

最后迁移一下数据即可！