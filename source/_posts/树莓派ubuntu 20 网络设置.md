---
title: 树莓派ubuntu 20 网络设置
date: 2020-09-05 17:49:26
author: Ginta
img: http://img.ginta.top/dm2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/dm2.jpg
toc: false
mathjax: false
summary:
tags: 
  - 树莓派
categories: 树莓派
---
## 前言

在树莓派4B上配置一个 *ubuntu 20 LTS* 网络环境折腾了挺久的，在此记录一下以免下次再次采坑。

```

# 编辑 /etc/netplan/50-cloud-init.yaml 改成如下

network:

    ethernets:

        eth0:

            dhcp4: true

            optional: true

    version: 2

    wifis:

        wlan0:

            access-points:

                "Danke42168_1":  # 这个是wifi名字

                    password: "wifi.danke.life"   # 这是wifi密码

            dhcp4: true

            optional: true

```

## 最后

如果没有显示器可以先修改 root文件夹下的 **network-config** 文件， **一定要在第一次开机前设置，否则无法生效**。不过由于安装包用的是国外的源，所以一般还是要接上显示器来配置国内源

如果想设置固定ip可以追加配置，最终配置如下：

```

# This file is generated from information provided by the datasource.  Changes

# to it will not persist across an instance reboot.  To disable cloud-init's

# network configuration capabilities, write a file

# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:

# network: {config: disabled}

network:

    ethernets:

        eth0:

            dhcp4: true

            optional: true

    version: 2

    wifis:

        wlan0:

            access-points:

                "Danke42168_1":

                    password: "wifi.danke.life"

            dhcp4: true

            optional: true

            addresses: [192.168.124.18/24]

            gateway4: 192.168.124.1

            nameservers:

                addresses: [192.168.124.1, 8.8.8.8]

```