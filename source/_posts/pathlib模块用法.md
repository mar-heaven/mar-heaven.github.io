---
title: pathlib模块用法
date: 2020-05-07 14:51:52
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
  - python
categories: python
---
## 前言
*Python* 中对于路径处理有一个 **os.path** 模块，基本上所有常见的需求都可以满足，不过也有一些弊端
```
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```
以上用法在 **Django** 项目中应该是十分常见的，阅读起来非常不方便。
## 福利
在 **python3.5** 之后引入了一个新的内置包 **pathlib**。有了它很多操作都会变得简单明了，直接上代码：
上述的例子如果用 **pathlib** 可以写成如下样子：
```
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR.joinpath('templates')
```

其他用法：
```
# 路径拼接
Path('D:/test','pb','123.txt')
# WindowsPath('D:/test/pb/123.txt')

# 分割路径
from pathlib import PurePath
p = PurePath('/usr/bin/python3')
p.parts
# ('\\', 'usr', 'bin', 'python3')

# 获取指定类型的文件
p = Path('.')
list(p.glob('*.py'))
# [WindowsPath('day_close_not_equal_min.py'), WindowsPath('day_h5.py'), WindowsPath('local_run.py'), WindowsPath('min_h5.py'), WindowsPath('min_h5_1.py'), WindowsPath('prev_iopv2tick.py'), # # # 
# WindowsPath('read_h5.py'), WindowsPath('repair_close.py'), WindowsPath('rep_nan.py
```

## 结语
基本上 **os.path** 中常用的方法在 **pathlib** 都可以找到，而且面向对象的思想更容易被理解，代码也会相对清晰一些。