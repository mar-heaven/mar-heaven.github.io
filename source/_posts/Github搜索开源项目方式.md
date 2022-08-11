---
title: Github搜索开源项目方式
date: 2020-05-02 12:37:28
author: Ginta
img: http://img.ginta.top/sky2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/sky2.jpg
toc: false
mathjax: false
summary:
tags: 
categories: Git/Github
---
### 前言
作为全球最大的同性交友网站，**Github** 上有很多优秀的开源项目，使用正确的方式搜索可以很方便地找到自己需要的资源。

### 使用
筛选的语法非常简单
```
# 按照项目名/仓库名搜索（大小写不敏感）
in:name xxx 
# 按照README搜索（大小写不敏感）
in:readme xxx
# 按照description搜索（大小写不敏感）
in:description xxx
# stars数大于xxx
stars:>xxx
# forks数大于xxx
forks:>xxx
# 编程语言为xxx
language:xxx
# 最新更新时间晚于YYYY-MM-DD
pushed:>YYYY-MM-DD
```
举个例子，如果需要搜索一个基于 *Django* 的后台管理项目，可以通过以下方式，搜索仓库名包含 **django** 关键字并且项目描述中包含 **后台**  关键字。
![](http://img.ginta.top/markdownx/2020/04/22/27c4d6a1-e8f3-40b1-8b14-93eb48715f1e.png)
就是这么方便，当然可以通过更新时间来过滤一些不维护的项目。