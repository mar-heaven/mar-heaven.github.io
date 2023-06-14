---
title: ubuntu 部署 django2.0 + uwsgi + nginx
date: 2019-11-27 03:02:12
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
  - Django
  - 自动化
  - uwsgi
categories: Django
published: false
---
###

*django* 默认的服务是单进程的，而且处理静态文件也比较慢，我们采用 **django + uwsgi + nginx** 来提高并发数的同时减少静态文件的访问时间。



### nginx

1. 安装nginx

`apt-get install nginx`

2. 进入 **/etc/nginx** 路径下可以看到两个文件夹，**sites-available** 和 **sites-enabled**，前者是网站的可用配置文件夹，后者是启用的配置，一般都是把配置文件放到 **sites-available** 再通过软链接的方式在 **sites-enabled** 中启用配置。

3. 进入 **sites-available** 文件夹中，新建配置文件arrange.conf，内容如下

```

server {

    listen 80;     # 网站对外的端口为80

    server_name ginta.top;  # 服务名字（一般是用域名方便理解）

    charset utf-8;   # 字符编码



    client_max_body_size 75M;     # 上传文件的最大尺寸



    location /static {

        alias /home/admin/code/Workspace/arrange/static;      # 静态文件的访问路径

    }

    

    location /media{

        alias /home/admin/code/Workspace/arrange/media;      # 媒体资源的访问路径

    }



    location / {                  # 发送请求给django，nginx处理不了，我们要转发给uwsgi，除了 static 和 media 其他的转发给uwsgi

        uwsgi_pass 127.0.0.1:8001;

        include /etc/nginx/uwsgi_params;  # uwsgi协议配置文件，类似于nginx.conf，django没有，但是nginx下有个这样的文件

    }

}

```

4. 删除 **sites-enabled** 文件夹下的default文件，否则服务可能无法启动，卡在nginx欢迎界面



![在这里插入图片描述](https://img-blog.csdnimg.cn/20190826214047909.png)





### uWSGI

1. 安装uWSGI，可能出现的错误在这里有 [解决方式](https://blog.csdn.net/qq_35068933/article/details/100049788). 

```pip install uwsgi```

2. 测试，创建一个 **foobar.py** 的文件，内容如下 :

```

def application(env, start_response):

    start_response('200 OK', [('Content-Type','text/html')])

    return [b"Hello World"]

```

然后通过服务器的 *9090* 端口进行测试

`uwsgi --http :9090 --wsgi-file foobar.py`

访问成功即可。

3. 编写项目uwsgi配置文件

然后选择一个目录新建个文件作为项目的 *uwsgi* 配置文件,我这里是 **arrange.ini**

```

[uwsgi]

chdir = /home/admin/code/Workspace/arrange  # 项目的绝对路径

virtualenv = /home/admin/code/Envs/blog       # 我这里用的是虚拟环境

module = arrange.wsgi:application     # 项目的wsgi，我的项目名是 **arrange**



master = True   #  启动主程序

processes = 4  # 使用的进程数

harakiri = 60   # 请求60s超时关闭

max-requests = 5000    # 请求超过5000进程重启防止内存泄漏

 

socket = 127.0.0.1:8001   # 监听的端口

uid = nginx  #  使用nginx代替root用户 （安全一些）      

gid = nginx  #  使用nginx代替root用户     



pidfile = /home/admin/mysite_uwsgi/master.pid     # 通过 pidfile 对主进程进行关闭，启动或者重启操作

daemonize = /home/admin/mysite_uwsgi/arrange.log  # 指定日志存放路径

vacuum = True # 当服务器关闭会自动把pidfile和daemonize进程回收

```

4. 启动项目uwsgi

`uwsgi --ini arrange.ini`

5. 进入 **/etc/nginx/** 路径，简历配置文件软链接

`sudo ln -s /etc/nginx/sites-available/arrange.conf /etc/nginx/sites-enabled/arrange.conf`

6. 测试一下nginx有没有问题

`sudo nginx -t`

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190826214422441.png)

出现 **successful** 表示没有问题

7. 重启nginx

`sudo service nginx restart`



### 补充

**uwsgi** 重启服务,由于我们配置了pidfile路径，所以可以很快捷地重启

`uwsgi --reload /home/admin/mysite_uwsgi/master.pid`

想看看启动没有可以通过 **ps** 指令

`ps -aux | grep uwsgi`

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190826215035845.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)