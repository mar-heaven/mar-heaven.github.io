---
title: Windows10 docker desktop k8s
date: 2020-11-14 23:30:16
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
  - docker
  - windows
  - k8s
categories: 其他
---
##前言
家里的台式机换了主板，cpu和内存之后流畅很多，图形化界面是 *Windows* 系统天然的优势，所以装了个 *docker desktop*，装完后发现可以一键安装k8s，果断开干。

虽说是一键，但还是有个小问题。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201114232406748.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70#pic_center)
一起在启动中，等了很久都没反应，猜测是因为依赖都是外网，需要开代理。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201114232518138.png#pic_center)
我的本机代理端口是1080。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201114232548120.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70#pic_center)
最终成功安装！
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201114232758702.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70#pic_center)
可能有细心的发现 *k8s* 版本变了，是因为我已经成功安装，看不到 *starting* 了，于是在网上找了一张，不过这不重要~

## 2021.3.12
`docker pull` 用的是https
之前imac上的k8s一直无法启动，配置了 *https* 代理就好了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210312164920909.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)
