---
title: Borg状态共享
date: 2020-09-26 15:54:30
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
  - python
categories: python
---
## 前言
有一个类 **Singleton** ，我们需要它所有的子类，以及子类的子类所有实例共享同一状态。
```
class Singleton(object):
    state = 1
    def __init__(self, state):
        self.state = state

class SingletonA(Singleton):
    pass

class SingletonB(Singleton):
    pass

a = SingletonA(1)
b = SingletonB(2)


a = SingletonA(1)
b = SingletonB(2)
print("a.state:", a.state)
print("b.state:",b.state)
a.state = 666
print("new a.state:",a.state)
print("new b.state:",b.state)
```
输出结果
```
a.state: 1
b.state: 2
new a.state: 666
new b.state: 2
```
可以看到，虽然我们把 *a* 的状态改变了，但是 *b* 的状态并没有改变
## 解决
如果我们想做到修改 *a* 的状态以后， *b* 的状态也随之修改，可以使用 **Borg** 模式，从父类的 *__dict__* 入手
```
class Borg(object):
    state = 0
    __share_dict = {}
    def __init__(self, state):
        self.__dict__ = self.__share_dict
        self.state = state
class BorgA(Borg):
    pass

class BorgB(Borg):
    pass

old = Borg(7)
a = BorgA(1)
b = BorgB(2)
print("old.state:", a.state)
print("a.state:", a.state)
print("b.state:",b.state)
a.state = 666
print("new old.state:",a.state)
print("new a.state:",a.state)
print("new b.state:",b.state)
```
## 输出
```
old.state: 2
a.state: 2
b.state: 2
new old.state: 666
new a.state: 666
new b.state: 666
```
显然，当我们声明  `self.__dict__ = self.__share_dict` 的时候，所有 **Borg** 以及他的子类实例就共享同一个 **state** 属性了。