---
title: django Signals
date: 2019-11-27 03:00:17
author: Ginta
img: http://img.ginta.top/huoying2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/huoying2.jpg
toc: false
mathjax: false
summary:
tags: 
  - Django
categories: Django
---
### 前言
在平时应用中我们经常遇到比如新增加一个用户就发送短信，新增加一条留言就给我们 **发送邮箱** 这种需求，一般来说都可以在视图函数中完成这些操作。但是如果有多个地方都需要类似的操作，比如用户在N个应用中都可以留言，如果在每个视图函数中都写一遍 **发送邮箱** 这种操作无疑是不明智的，好在 *django* 框架中内置了 **signals(信号)** 机制，可以辅助我们监听某些行为，比如 *model* 新增，或者请求前和请求后。


### 信号
官方的信号主要分为以下几种，具体介绍详见 [Django信号](https://docs.djangoproject.com/en/2.2/ref/signals/)。
1. Model signals
 - pre_init
- post_init
- pre_save
- post_save
- pre_delete
- post_delete
- class_prepared
2. Management signals
- post_syncdb
3. Request/response signals
- request_started
- request_finished
- got_request_exception
4. Test signals
- template_rendered


### 举例
这里举一个例子，官方推荐在应用目录下新增一个 signals.py文件
1. 新建并注册app，我这里app名字是 *signalapp*
2. 在app下方新建signals.py文件
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191114002302755.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)
4. 修改 app下面的 apps.py
```python
# 原来
from django.apps import AppConfig

class SignalappConfig(AppConfig):
    name = 'signalapp'
```

```python
# 现在
from django.apps import AppConfig

class SignalappConfig(AppConfig):
    name = 'signalapp'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import signalapp.signals
```
4. 编写 signals.py
```python
# signalapp/signals.py
from django.dispatch import receiver
from django.db.models.signals import post_save
from signalapp.models import Post

def send():
    print("发送邮件")

@receiver(post_save, sender=Post, dispatch_uid='Post_post_save')
def send_email(instance, **kwargs):
    send()
```
然后重启服务，接下来在任意地方只要新建了 **Post** 实例并保存了，该函数都将在保存之后执行。与之相对应的是函数是 **pre_save**，显然，这是在保存前执行的。 *receiver* 装饰器有三个参数：
1. 第一个是要监听的信号，我这里是 post_save
2. 第二个是所要监听的模型，我这里是 Post 是文章模型，所以这个函数会在每次有文章保存（新建或者更新）的时候触发
3. post_save 在某个Model保存之后调用, 对于每个唯一的dispatch_uid,接收器都只被信号调用一次

这个信号的功能就是每次新建或者更改文章的时候发送一个邮件（邮件函数没写。。）

## 补充
其他的可以参考文档，*django* 的文档写得确实很好，另外想说的就是 *sender* 不一定是模型，也可以是函数：
```python
import datetime
import os
import django
from django.dispatch import receiver, Signal
from django.http import HttpResponse

# 发送信号
def signal_sender(request):
    hostname = request.get_host()
    msg = 'Django Signal Test'
    time = datetime.date.today()
    signal_obj.send(sender=signal_sender, hostname=hostname, msg=msg, time=time)     # 关键一行
    return HttpResponse('200 OK')


# 接收和处理信号
@receiver(signal_obj, sender=signal_sender)       # 装饰器把处理函数注册成接收器
def signal_handler(sender, **kwargs):　　　　　　   # 接收到信号后，在此处理。kwargs字典用来传递Signal信号参数
    print('接收到信号内容：{hostname}|"{msg}"|{time}'.format(hostname=kwargs['hostname'], msg=kwargs['msg'], time=kwargs['time']))
```