---
title: ubuntu python3.7 安装uwsgi 常见错误
date: 2019-11-27 02:03:56
author: Ginta
img: http://img.ginta.top/fantasy2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/fantasy2.jpg
toc: false
mathjax: false
summary:
tags: 
  - python
categories: python
published: false
---
### 前言

由于需要在 *ubuntu18.04* 系统部署 *django* 项目，用到了 *uWSGI* 库，在安装的时候遇到了几个问题在这里记录一下原因，并附上解决方法。



### Retrying (Retry(total=4, connect=None....

这是比较常见的问题，原因是安装超时，因为我们下载的库的源一般都是在国外，涉及到翻墙问题，解决方法是更换国内的源，注明的有阿里，豆瓣等，这里我用到的是豆瓣源:

```pip install -i https://pypi.doubanio.com/simple uwsgi```

前面 **-i** 是指明更换源路径，最后的 **uwsgi** 就是本次我要安装的 **uWSGI** 库



### error: invalid command 'bdist_wheel'

这个问题一般是 **pip** 版本比较老了，更新一下即可

尝试用以下命令升级以下pip版本后再试一下:

python -m pip install --upgrade pip

如果装着python3.X ，那么就用:

python3 -m pip install --upgrade pip





### fatal error: Python.h

网上说的是因为环境不完整，安装如下这个包：

python2：

```sudo apt-get install python-dev```

python3:

```sudo apt-get install python3-dev```

确实是这个问题，不过可能是我的 *python* 版本比较新吧，是 *python3.7.2* ，也可能是其他原因总之最后安装 *uWSGI* 还是失败了，网上还有一个库是真的比较新版本的 *python3.7+* ：

```sudo apt install python3.7-dev```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190824103651540.png)

安装成功~