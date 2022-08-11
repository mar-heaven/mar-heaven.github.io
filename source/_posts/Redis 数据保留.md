---
title: Redis 数据保留
date: 2019-11-27 01:58:59
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
categories: 数据库
---
## Windows
所谓数据丢失是因为 *redis* 有个专门保存数据的文件，而这个文件一开始是只读的，我直接把整个 *Redis* 文件夹的权限都开放给当前用户，这样退出时数据就会保留下来了。还有就是启动时要用`redis-server.exe redis.windows.conf`命令。