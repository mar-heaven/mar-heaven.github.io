---
title: supervisor + pipenv + uwsgi
date: 2019-11-20 03:28:48
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
  - python
  - Django
  - 自动化
categories: Django
published: false
---
## 前言

目前我部署 *django* 项目的方式是 *uwsgi + nginx* ，*uwsgi* 重启也很方便，只需要写一句 *uwsgi --reload xxx.pid* 即可，但是即使是一句我也不想输入了，就是比较懒，于是乎就有了 **supervisor** 管理 *uwsgi* 进程，配置好以后通过 *web* 网页点一下即可。

## 开始

至于怎么配置 *uwsgi* 网上教程有很多，这里只讲一下怎么用 *supervisor* 启动。

通过网上的教程可以先安装好 *supervisor* ，我这里有一篇 **[ubuntu python3 配置 supervisor](https://blog.csdn.net/qq_35068933/article/details/103087914)** 可供参考。我的 *supervisor* 配置目录结构如下：

```

supervisor/

├── conf.d

│   ├── myblog.ini   # 自己配的

├── supervisord.conf   # 初始化生成的配置文件（一开始就有，网上可以找到如何生成）

└── var

    ├── log

    │   ├── myblog-stderr.log      # 后续生成的

    │   ├── myblog-stdout.log	   # 后续生成的

    │   └── supervisord.log   # 后续生成的

    ├── supervisord.pid   # 后续生成的

    └── supervisor.sock   # 后续生成的



```

*supervisor* 文件夹是在 **/etc** 下面。

首先配置 **supervisor/supervisord.conf** 文件，有几个地方改了一下：

1.  让 socket 文件生成在 ~/etc/supervisor/var/ 目录下。**注意 supervisor 不支持将 ~ 展开为用户 home 目录，所以要用绝对路径指定。我这里是 *root* 用户，这样直接写就可以，其他用户的路径类似于 /home/username/etc/supervisor...****

```

[unix_http_server]

file=/etc/supervisor/var/supervisor.sock   ; the path to the socket file

```

2. 修改 [inet_http_server] ，这一步主要是可以通过外部浏览器来进行控制 supervisor 进程，其中 端口号像我这样配置成 port=*:9001 ，就可以在外网通过服务器的域名下的 *9001* 端口来控制，默认是没有密码的，但是最好配置一下

```

[inet_http_server]         ; inet (TCP) server disabled by default

port=*:9001        ; ip_address:port specifier, *:port for all iface

;username=user              ; default is no username (open server)

;password=123               ; default is no password (open server)

```

3.  类似的修改 [supervisord] 板块下的 logfile 和 pidfile 文件的路径，还有 user 改为系统用户，这样 supervisor 启动的进程将以系统用户运行，避免可能的权限问题,**注意 supervisor 不支持将 ~ 展开为用户 home 目录，所以要用绝对路径指定。我这里是 *root* 用户，这样直接写就可以，其他用户的路径类似于 /home/username/etc/supervisor...**：

```

[supervisord]

logfile=/etc/supervisor/var/log/supervisord.log ; main log file; default $CWD/supervisord.log

pidfile=/etc/supervisor/var/supervisord.pid ; supervisord pidfile; default supervisord.pid

user=root            ; setuid to this UNIX account at startup; recommended if root

```

4.   [supervisorctl]板块下：

```

[supervisorctl]

serverurl=unix:///etc/supervisor/var/supervisor.sock ; use a unix:// URL  for a unix socket

```

5. [include] 版块,将 /etc/supervisor/conf.d/ 目录下所有以 .ini 结尾的文件内容包含到配置中来，这样便于配置的模块化管理。

```

[include]

files = /etc/supervisor/conf.d/*.ini

```

7. 配置 **管理uwsgi进程** 的配置文件

在 **/etc/supervisor/conf.d/** 目录下新建一个配置文件，名字以 *.ini* 结尾就好，是因为我们在 *supervisor.conf* 文件中修改了配置 [include] ，所以 *supervisor* 会搜索  */etc/supervisor/conf.d/* 目录下所有以 *.ini* 结尾的文件。

这是我的配置文件

```

[program:myblog]

command=pipenv run uwsgi --ini /root/mysite_uwsgi/myblog.ini

directory=/root/code/Workspace/ginta.top

autostart=true

autorestart=unexpected

user=root

stdout_logfile=/etc/supervisor/var/log/myblog-stdout.log

stderr_logfile=/etc/supervisor/var/log/myblog-stderr.log

```

program:hellodjango-blog-tutorial] 指明运行应用的进程，名为 hellodjango-blog-tutorial。



command 为进程启动时执行的命令， 我的环境是用 pipenv 来进行包管理的所以要这样执行，如果没有用包管理直接执行 `uwsgi --ini /root/mysite_uwsgi/myblog.ini` 即可，也就是 *uwsgi* 的启动命令。



directory 指定执行命令时所在的目录。



autostart 随 Supervisor 启动自动启动进程。



autorestart 进程意外退出时重启。



user 进程运行的用户，防止权限问题。



stdout_logfile，stderr_logfile 日志输出文件。

6. 启动 Supervisor

```

supervisord -c ~/etc/supervisord.conf

```

7. 进入 supervisorctl 进程管理控制台：

```

supervisorctl -c ~/etc/supervisord.conf

```

执行 update 命令更新配置文件并启动应用。



浏览器输入域名，可以看到服务已经正常启动了。



## 注意

1. 由于我们 **supervisor** 有配置项目的日志，所以如果在 **uwsgi.ini** 中配置有日志，请把它注释掉

```

# myblog.ini （项目的uwsgi配置）

# daemonize = /root/mysite_uwsgi/myblog.log             # 日志管理

```

2. **如果之前就已经运行了 uwsgi，请一定要先退出再重启 supervisor**

3. *supervisor/supervisord.conf* 文件的注释符号是 **;**，比如 *;[eventlistener:theeventlistenername]*，所以我们所有的配置前面如果有 **;** ，请删掉，比如把 *;[eventlistener:theeventlistenername]* 改成 *[eventlistener:theeventlistenername]* ，不然会视作没有配置。



本文配置参考了[追梦人物的博客](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/74/)。