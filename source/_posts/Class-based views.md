---
title: Class-based views
date: 2019-11-23 12:17:31
author: Ginta
img: http://img.ginta.top/dragin1.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/dragin1.jpg
toc: false
mathjax: false
summary:
tags: 
  - Django
categories: Django
published: false
---
### 前言 

*Django* 中 **函数视图** 中有个 *request* 对象，封装了一些请求的数据，比如 **post** 请求上传来的参数或者当前用户数据：

```

def index(request, *args, **kwargs):

    print(args)

    return HttpResponse("hello")

```

在给博客新增第三方登录的时候后端要进行一些用户数据的处理，比如头像链接拼接，而项目的视图函数采用的是 **类视图**。

### 解决

一开始没有找到 **User** 对象，然后看了看 *View* 类的封装，发现有这么一段：

```

def setup(self, request, *args, **kwargs):

    """Initialize attributes shared by all view methods."""

    self.request = request

    self.args = args

    self.kwargs = kwargs

```

显然在 **类视图** 中 **request** 对象被封装成一个属性了，那调用的时候就用 **self.request** 来代替原来的 **request**，比如获取当前用户就用 **self.request.user** 即可。



### 结语

遇到问题直接看源码有时候比百度要来得快一些。