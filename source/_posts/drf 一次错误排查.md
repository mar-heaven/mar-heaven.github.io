---
title: drf 一次错误排查
date: 2020-02-12 16:53:52
author: Ginta
img: http://img.ginta.top/chaoshou2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/chaoshou2.jpg
toc: false
mathjax: false
summary:
tags: 
categories: Django
---
## 前言
在使用最新版本的 *DRF* 框架时，注册路由阶段报了一个错
>>>
“django.core.exceptions.ImproperlyConfigured: The included URLconf 'bingo.urls' does not appear to have any patterns in it. If you see valid patterns in the file then the issue is probably caused by a circular import.” 

找了半天错误，期间反复查看官方文档都没有什么问题，最后使用删减排除了错误,原本用户的路由是这个
```
user_router.register("user", UserViewSet, base_name="user")
```
结果报错了，我改成以下代码：
```
user_router.register("user", UserViewSet)
```
问题得到了解决，然而还是睡不着，这个参数在使用中还是很方便的，就这么删掉了肯定不好，于是上 *github* 查看了该项目的 *issues*，最后发现新版本的 *base_name* 已经被替换了：


![](http://img.ginta.top/markdownx/2019/12/02/05741e40-c072-41e6-8d32-802e5e201f9b.png)
于是把 *base_name* 改成了 *basename*，问题解决！