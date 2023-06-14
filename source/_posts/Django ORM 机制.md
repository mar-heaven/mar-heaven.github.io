---
title: Django ORM 机制
date: 2020-02-19 03:35:32
author: Ginta
img: http://img.ginta.top/qinshi2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/qinshi2.jpg
toc: false
mathjax: false
summary:
tags: 
  - Django
categories: 数据库
published: false
---
## *ORM*是什么

目前大多数互联网项目都涉及到数据库，不同的数据库有着自己的优势，用的时候就需要查询它们的 *sql* 语句，学习成本高；另外一段很长的 *sql* 语句很容易存在被注入的风险。



**对象关系映射**（Object Relational Mapping，简称**ORM**）模式是一种为了解决面向对象与关系数据库存在的互不匹配的现象的技术。



该技术让我们可以使用面向对象的方法来进行数据库的操作，从而不必理会不同数据库之间 *sql* 语句的差异。





![ORM示意图](http://img.ginta.top/markdownx/2019/12/02/23d52908-3a2b-45ae-a4b2-f761781d870e.png)



如上图所示，类对应的就是数据库中的表，类中的属性对应数据表中的字段，类的实例对象就是数据库中的一条条数据了。



```

from django.db import models



class Person(models.Model):

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)

```

这里的 **Person** 在数据库中就是一张表，表名可以自定义。*first_name* 和 *last_name* 就是其中的两个字段，*max_length* 就是长度约束，比如 *MySQL* 数据库中对于字符字段可以设置其最大长度。

如果我们想新建一条数据，可以通过以下方法：

```

from .models import Person

person = Person(first_name="泷谷", last_name="源治")

person.save()

```



## 总结

**ORM** 让开发人员大大减少了工作量，使得代码更加清晰，方便维护。当然每个技术有优点就有缺陷，**ORM** 虽然使开发效率提高了，但是缺牺牲了一些性能；另外一些复杂的 *sql* 语句并不能通过 **ORM** 来实现。不过对于大多开发者来说还是利大于弊。