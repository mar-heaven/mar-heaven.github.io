---
title: win10 osg.js 使用
date: 2019-12-03 09:02:07
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
categories: 其他
published: false
---
## 引言

有位朋友希望可以在win10上部署一个 *osg.js* 服务，虽然在这之前我也没用过 *osg.js* ，不过看了下官方基本的 doc，由于是涉及到美术行业内容不是很懂，不过部署貌似也不复杂。



## 安装依赖

该工程一共需要2个依赖，一个是 *Git* ，另外就是 *npm*。

首先安装 **Git** ，点击此处的[下载链接](https://github.com/git-for-windows/git/releases/download/v2.24.0.windows.2/Git-2.24.0.2-64-bit.exe)下载安装包，一直下一步就好。其次安装 **npm**，这里参考[廖雪峰教程](https://www.liaoxuefeng.com/wiki/1022910821149312/1023025597810528)就可以。



## 下一步

这是[官方链接](http://osgjs.org)，部署非常简单，首先在电脑上安装一个 *git* 把代码 *clone* 下来，找一个存放工程的目录，右键，点击 *Git Bash Here*：





![](http://img.ginta.top/markdownx/2019/12/02/d520a651-7ef9-416e-8653-2f32b628c933.png)



然后执行 `$ git clone git://github.com/cedricpinson/osgjs.git`，接下来就可以在目录下看到一个 **osgjs** 文件夹。接下来进入这个文件夹 `$ cd osgjs/`，依次执行四条命令：



- `npm install -g grunt-cli`

- `npm install`

- `grunt build`

- `grunt serve`

不出意外可以看到这个界面



![](http://img.ginta.top/markdownx/2019/12/02/57c92fc4-0753-4b90-8308-899de31ad4fd.png)

打开浏览器访问 `http://localhost:9000/` ，然后就可以体验了





![](http://img.ginta.top/markdownx/2019/12/02/244e4c99-6b42-4d73-adb6-18dba844ca5a.png)



虽然不是这个方向，但感觉还是挺不错的。



## 小结

整个过程还是挺简单的，最费时间的是执行 `grunt serve` 这一步，因为要从其他仓库下载模型，而且还是外网，所以非常耗时，建议采用 **科学上网** 的方式执行。我当时执行这一步的时候真的是失败了N次，但是想着答应要尽力的，最终还是耐心多尝试，最后成功了，挺高兴的。