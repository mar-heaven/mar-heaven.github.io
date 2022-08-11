---
title: Linux文件属性
date: 2020-02-18 05:44:05
author: Ginta
img: http://img.ginta.top/dm3.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/dm3.jpg
toc: false
mathjax: false
summary:
tags: 
categories: Linux
---
## 前言
以前一直只知道 *chmod + 777 文件或者目录* 就是把文件或者文件夹的权限提升到所有人都可以使用，至于为什么是 *777* 一直没有了解过，最近在看 《鸟叔的Linux私房菜-基础篇》，记录下这部分。
## 查看文件属性
执行 `ls -al` 来查看一个目录下的文件和文件夹（包含隐藏的）属性。

![](http://img.ginta.top/markdownx/2019/12/02/89715ab9-d277-4c12-8f71-6cfa1b4bd987.png)

分为七部分，以最后一行说明

1.  -rw-r--r-- 文件的类型权限，一共十个字母。第一个字母是文件类型， *-* 表示是个文件，*d* 表示是个目录。后面九个每三个分为一组，表示执行权限,[rwx]分别表示可读，可写，可执行：第一组是文件所有者的权限，第二组是此所有者所在的组权限，第三组是非本人且没有加入本人所在组的权限。
2. 第二个为连接到此节点的链接数，包括硬链接和软链接
3. 第三个是文件（目录）所属用户 
4. 第四个是文件所在的群组
5. 第五个是文件大小
6. 第六个是文件创建日期
7. 第七个是文件名

## 改变文件属性和权限
1. chgrp: 改变文件所属群组
2. chown: 改变文件拥有者
3. chmod: 改变文件权限，SUID, SGID, SBIT 等等的特性

### 改变文件所属组
`chgrp users myblog.ini`
把 *myblog.ini* 文件所在组改为 *uses*，如果组不存在则会报错

### 改变文件的拥有者
`chown ginta myblog.ini`
把 *myblog.ini* 文件拥有者改为 *ginta*

### 改变文件的权限 
Linux文件一共有9个基本权限，分别是owner/group/others三个身份以及read/write/execute三个权限，三个三个为一组可以排列出9种权限。
- r:4
- w:2
- e:1
其中身份(owner/group/others)和权限(r/w/x)是累加的， 比如我们上边的 [-rw-r--r--] 就代表

- owner = -rw = 0 + 4+2 =6
- group = r-- = 4 +0 + 0 = 4
- others = r-- = 4 + 0 + 0 = 4
那么此文件的权限就是 644
修改文件权限的命令是
`chmod 777 myblog.ini`
这条命令就是我之前无脑操作的，权限全开。

## 总结
以前的文件操作方式相当于把文件整个暴漏给了其他人，可读可写！！无知是多么可怕~