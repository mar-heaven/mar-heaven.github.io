---
title: 树莓派固定ip设置
date: 2020-05-30 15:04:43
author: Ginta
img: http://img.ginta.top/dragin1.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/dragin1.jpg
toc: false
mathjax: false
summary:
tags: 
categories: 树莓派
---
### 前言
由于没有多余的屏幕以及鼠标和键盘等外设（就是有也没空间放），所以树莓派只能通过 **xshell** 连接，先前我是可以连接上的，但是由于 *ip* 发生了变化所以又要重新连上屏幕查看 *ip*，但是以后难免还会发生这样的事情。一劳永逸的方法是设置一个固定 *ip* 这样下次登录就不会发生之前的问题了。
### 步骤
操作也很简单
树莓派中有个文件可以实现固定 *ip* 的设置，执行  `vim /etc/dhcpcd.conf`，修改配置文件
```
# 在最后加入下面几行
# 指定接口 wlan0
interface wlan0
# 指定静态IP，/24表示子网掩码为 255.255.255.0
static ip_address=192.168.124.18/24
# 路由器/网关IP地址
static routers=192.168.124.1
# 手动自定义DNS服务器
static domain_name_servers=114.114.114.114
```
然后执行 `sudo reboot` 即可，之后便可以通过 *xshell* 等工具进行连接
这里有两点需要注意
1. 我的路由器 *ip* 是 *192.168.124.1* ，但是常见的一般是 *192.168.1.1* 和 *192.168.0.1*
2. static ip_address=192.168.124.18/24，这一项要保证 **18端口没有被占用**，简单的方法就是 *ping 192.168.124.18* 如果没有响应就可以了

## 其他
至于树莓派怎么连接 *wifi* 参考 [无屏幕和键盘配置树莓派WiFi和SSH](https://shumeipai.nxez.com/2017/09/13/raspberry-pi-network-configuration-before-boot.html)。