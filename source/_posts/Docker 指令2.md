---
title: Docker 指令2
date: 2019-12-20 04:26:42
author: Ginta
img: http://img.ginta.top/fantasy1.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/fantasy1.jpg
toc: false
mathjax: false
summary:
tags: 
categories: docker
---
- RUN 执行命令并创建新的Image layer
- CMD 设置容器启动后默认执行的命令和参数
- ENTRYPOINT 设置容器启动时执行的命令

+ shell 格式
```
RUN apt-get install -y vim 
CMD echo "hello docker"
ENTRYPOINT echo "hello docker"
```

+ Exec格式
```
RUN ["apt-get", "install", "-y", "vim"]
CMD ["/bin/echo", "hello docker"]
ENTRYPOINT ["/bin/echo", "hello docker"]
```