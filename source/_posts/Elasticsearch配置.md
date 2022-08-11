---
title: Elasticsearch配置
date: 2019-12-28 14:24:42
author: Ginta
img: http://img.ginta.top/fantasy2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/fantasy2.jpg
toc: false
mathjax: false
summary:
tags: 
categories: 数据库
---
### 安装
1. Java环境
2. Git 下载 elasticsearch-rtf  压缩包，解压 进入bin 运行 elasticsearch.bat
3. Git clone elasticsearch-head 进入，npm install,npm run start
4. 配置elasticsearch.yml
```
http.cors.enabled: true
http.cors.allow-origin: "*"
http.cors.allow-methods: OPTIONS, HEAD, GET, PUT, DELETE
http.cors.allow-headers: "X-Requested_With, Content-Type, Content_Length, X-User"
```
5. 安装 kibana ,版本与 elasticsearch相对应

### elasticsearch概念
1. 集群
2. 节点
3. 分片
4. 副本


Elasticsearch | Mysql
---|---
index | 数据库
type | 表
documents | 行(一条数据)
fields | 列