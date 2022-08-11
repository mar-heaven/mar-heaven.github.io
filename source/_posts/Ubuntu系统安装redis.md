---
title: Ubuntu系统安装redis
date: 2019-11-27 02:00:44
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
  - redis
categories: 数据库
---
### 前言
一般爬虫是在 *Ubuntu* 系统下进行配置的，这次的任务就是在 *Ubuntu* 系统下安装 *redis*。

### 步骤
- `sudo apt-get install redis-server`，遇到依赖包输入 *Y* 回车即可
- 启动，安装以后自动启动，可以查看 `ps aux|grep redis`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190505003642237.png)
- 手动启动， `sudo service redis-server start`
- 停止， `sudo service redis-server stop`
### 卸载
`sudo apt-get purge --auto-remove redis-server`

## Ubuntu连接Windows redis
我这里 *Windows* 用的是本机 *redis* 服务，*ubuntu* 使用的虚拟机，也就是说是在同一个局域网下的，不同网络其实也差不多，连接其他服务器 *redis* 的命令是 `redis-cli -h host -p port`，比如我的 *Windows* 局域网 *ip* 是 *192.168.199.168* 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190505011442356.png) 
*redis*端口是 *6379* ，那命令就是 `redis-cli -h 192.168.199.168 -p 6379`：
**ubunu** 下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190505010716614.png)
我们用 *ubuntu* 系统连接 *Windows* 系统 *redis* ，这里显示失败了，我们开 *windows* 的 *redis* 配置文件 *redis.windows.conf* 有这么一行
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019050501090661.png)
意思是其他人访问 *redis* 的时候地址是这个，我们都知道 *127.0.0.1* 永远指向本机，当然不能访问成功了，我们改成本机地址就可以，一定是当前局域网的 *ip*，也就是 *bind* 一定是**服务器**的 *ip* 地址，而不是客户端的 *ip*，如果是 **0.0.0.0** 表示其他机器可以通过本机的所有网卡（一台电脑可能有多个网卡） *ip* 地址连接本机 *redis*:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190505011052738.png)
保存之后重启 *windows* 的 *redis* 服务，再用 *ubuntu* 连接一下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190505011205854.png)
我们可以看到，成功了，并且访问 *username* 键，获得了它的值。