---
title: windows终端命令行下使用网络代理
date: 2020-05-05 02:44:02
author: Ginta
img: http://img.ginta.top/huoying1.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/huoying1.jpg
toc: false
mathjax: false
summary:
tags: 
categories: 其他
---
1. 右键打开 *ShadowsocksR* 的 **选项设置**


![](http://img.ginta.top/markdownx/2020/05/02/71045421-767e-438f-91a1-3e3d5be60fff.png)


2. 设置你的HTTP和HTTPS的代理端口

![](http://img.ginta.top/markdownx/2020/05/02/59a20c57-2d53-40fb-b559-93881dbe6f56.png)


3. 打开cmd窗口，设置代理变量
```
set HTTP_PROXY=http://127.0.0.1:1080
set HTTPS_PROXY=http://127.0.0.1:1080
```
如果设置了用户名和密码
```
set HTTP_PROXY=http://proxy.com:port
set HTTP_PROXY_USER=username
set HTTP_PROXY_PASS=password

set HTTPS_PROXY=http://proxy.com:port
set HTTPS_PROXY_USER=username
set HTTPS_PROXY_PASS=password
```
上面命令的作用是设置环境变量，不用担心，这种环境变量只会持续到cmd窗口关闭，不是系统环境变量。

如何取消代理呢:
```
netsh winhttp reset proxy
```