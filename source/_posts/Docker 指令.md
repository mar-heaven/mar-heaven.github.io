---
title: Docker 指令
date: 2019-12-20 04:24:55
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
categories: docker
---
1. docker images 显示所有镜像
2. docker build -t image_name .  (点就是从当前路径查找Dockerfile)
3. docker container ls 列举当前运行的容器
4. docker run -it image_name 交互式运行image
5. docker rm/docker container rm container_id 删除container
6. docker rmi/docker image rm image_id 删除image
7. docker container -aq 列出所有container_id (-q代表只列出id)
8. docker rm $(docker container -aq)    ($，删除所有列表中的元素)
9. docker rm $(docker container ls -f "status=exited" -q) 删除退出的容器
10. docker commit container_name new_container_name
    
    `docker commit frozty_jeew caesar123/centos-vim`
11. Dockerfile 用来build一个一模一样的image



### Dokerfile
- FROM strach # 制作base image
- FROM centos # 使用base image
- FROM ubuntu:14.04
- LABEL maintainer = "775650117@qq.com" (METADATA:注释)
- LABEL version = "1.0"
- RUN yum update && yun install -y vim \
  python-dev
- 每次运行RUN都会生成新的image，所以尽量合并成一行
- WORKDIR /root # 设定工作目录

```
WORKDIR /test # 如果没有会自动创建test目录     
WORKDIR demo
RUN pwd # 输出结果应该是/test/demo
```
- 用WORKDIR, 不要使用 RUN cd,尽量使用绝对目录
- ADD(COPY)
- ADD hello /
- ADD test.tar.gz / # 添加到根目录并解压
```
WORKDIR /root
ADD hello test/ # /root/test/hello
```
```
WORKDIR /root
COPY hello test/ # /root/test/hello
```
- 大部分情况，COPY优于ADD，ADD除了COPY还有解压功能
- 添加远程文件/目录请使用curl或者wget
- ENV MYSQL_VERSION 5.6 # 设置常量
```
ENV MYSQL_VERSION 5.6 # 设置常量
RUN apt-get install -y mysql-server= "${MYSQL_VERSION}" \
   && rm -rf /var/lib/apt/lists/* 引用常量
```
- 尽量使用ENV增加可维护性