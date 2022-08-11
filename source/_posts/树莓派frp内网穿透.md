---
title: 树莓派frp内网穿透
date: 2020-05-31 04:17:22
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
categories: 树莓派
---
### 前言
目的是实现外网连接树莓派

### 步骤
```
# 客户端（树莓派）frpc.ini 
[common]
server_addr = 120.79.215.235
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000
```
然后执行 `./frps -c ./frps.ini`

```
# 服务端（阿里云服务器） 
[common]

[common]
# 本机公网ip 120.79.215.235
bind_port = 7000
```
然后执行 `./frpc -c ./frpc.ini`


最后通过 *xshell* 连接
![](http://img.ginta.top/markdownx/2020/05/02/0d5c197a-a50b-47f1-a3e5-680e16ddc59d.png)

或者命令行 `ssh -oPort=6000 pi@120.79.215.235`
但是不知道为什么命令行的方式在 *xshell* 老提示密码错误。