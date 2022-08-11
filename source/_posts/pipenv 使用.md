---
title: pipenv 使用
date: 2019-11-27 02:02:10
author: Ginta
img: http://img.ginta.top/lc1.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/lc1.jpg
toc: false
mathjax: false
summary:
tags: 
  - python
categories: python
---
## 前言
以前做开发的时候一直使用的 *virtualenv* 作为虚拟环境库，当时也知道有其他工具，只是一直没有了解，在做项目的时候看到网上有一篇文章可以解决项目依赖库的问题：
比如说，之前有个项目开发使用的是 *django1.10* 版本，但是使用 `pip freeze >requirements.txt` 命令生成的文件中只有 *django* 没有具体哪个版本（现在貌似具体到版本了...），或者每次启动虚拟环境的时候都要输入一系列操作，现在只需要 `pipenv shell` 就可以了！
## 安装
- Windows系统下直接输入 `pip install pipenv`就可以了
- Ubuntu 系统下可能涉及到环境变量问题:具体步骤如下 
>运行python3 -m site(如果使用默认的可以运行 python -m site，这里我是python3)
>然后找到 **USER_BASE: '/root/.local' (exists)** ，然后在 **~/.profile** 最后一行加入 
>`export PATH=$PATH:/root/.local/bin`
>我是ubuntu系统，mac或者其他系统的 profile 文件到网上找找，最后执行 `source ~/.profile` 就可以了

## 使用
在任何地方执行 `pipenv install django` ，*pipenv* 会自动生成2个文件，分别是 *Pipfile* 和 *Pipfile.lock* ， *Pipfile.lock* 文件就会自动配置好 *django* 框架了：
```
  "default": {
      "django": {
          "hashes": [
              "sha256:4025317ca01f75fc79250ff7262a06d8ba97cd4f82e93394b2a0a6a4a925caeb",
              "sha256:a8ca1033acac9f33995eb2209a6bf18a4681c3e5269a878e9a7e0b7384ed1ca3"
          ],
          "index": "pypi",
          "version": "==2.2.6"
      },
    ....其他内容
```
激活虚拟环境的命令是 `pipenv shell`，需要注意的是，如果激活后使用 `pip install flask` 则只会在虚拟环境中安装 **Flask** 框架，并不会写入到 *Pipfile.lock* 配置中，如果想写入配置则执行 `pipenv install flask` 命令，然后如果需要生成 *requirements.txt* 文件则执行 `pipenv lock -r > requirements.txt` 命令，**只会打包 Pipfile.lock文件中的package**。

## 最后
一般来说在项目根目录下生成 *Pipfile* 和 *Pipfile.lock*  文件，方便后续操作，比如执行 *docker* 命令什么的都可以很简单安装好一个项目的依赖。