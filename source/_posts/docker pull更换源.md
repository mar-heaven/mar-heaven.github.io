---
title: docker pull更换源
date: 2020-08-30 14:29:59
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
  - docker
categories: docker
---
## 前言
每次使用docker pull的时候总是要等待很久，在不翻墙的情况下建议使用国内的源

## 步骤
1. 在 /etc/docker/daemon.json 文件中添加以下参数（没有该文件则新建）：
```
{
  "registry-mirrors": ["https://9cpn8tt6.mirror.aliyuncs.com"]
}
```
2. 服务重启
```
systemctl daemon-reload
systemctl restart docker
```