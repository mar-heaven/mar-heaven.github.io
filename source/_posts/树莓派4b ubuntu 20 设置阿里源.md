---
title: 树莓派4b ubuntu 20 设置阿里源
date: 2020-09-05 17:55:01
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
categories: 树莓派
---
## 前言
设置国内源其实很简单，但是由于我是下载的 64位 操作系统，并且树莓派是arm架构，所以有一点不同
执行 `lsb_release -a` 查看发行版本
```
ubuntu@ubuntu:/etc/netplan$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
```
所以修改配置文件 `sudo vim /etc/apt/sources.list`:
```
## Note, this file is written by cloud-init on first boot of an instance
## modifications made here will not survive a re-bundle.
## if you wish to make changes you can:
## a.) add 'apt_preserve_sources_list: true' to /etc/cloud/cloud.cfg
##     or do the same in user-data
## b.) add sources in /etc/apt/sources.list.d
## c.) make changes to template file /etc/cloud/templates/sources.list.tmpl

# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://mirrors.aliyun.com/ubuntu-ports focal main restricted
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://mirrors.aliyun.com/ubuntu-ports focal-updates main restricted
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://mirrors.aliyun.com/ubuntu-ports focal universe
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal universe
deb http://mirrors.aliyun.com/ubuntu-ports focal-updates universe
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team, and may not be under a free licence. Please satisfy yourself as to
## your rights to use the software. Also, please note that software in
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://mirrors.aliyun.com/ubuntu-ports focal multiverse
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal multiverse
deb http://mirrors.aliyun.com/ubuntu-ports focal-updates multiverse
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
deb http://mirrors.aliyun.com/ubuntu-ports focal-backports main restricted universe multiverse
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal-backports main restricted universe multiverse

## Uncomment the following two lines to add software from Canonical's
## 'partner' repository.
## This software is not part of Ubuntu, but is offered by Canonical and the
## respective vendors as a service to Ubuntu users.
# deb http://archive.canonical.com/ubuntu focal partner
# deb-src http://archive.canonical.com/ubuntu focal partner

deb http://mirrors.aliyun.com/ubuntu-ports focal-security main restricted
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal-security main restricted
deb http://mirrors.aliyun.com/ubuntu-ports focal-security universe
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal-security universe
deb http://mirrors.aliyun.com/ubuntu-ports focal-security multiverse
# deb-src http://mirrors.aliyun.com/ubuntu-ports focal-security multiverse
```

## 注意
由于是 **arm架构，一定要改成  http://mirrors.aliyun.com/ubuntu-ports 而不是  http://mirrors.aliyun.com/ubuntu，否则无法正常更新下载！！！**。