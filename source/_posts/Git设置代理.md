---
title: Git设置代理
date: 2020-03-31 12:12:18
author: Ginta
img: http://img.ginta.top/lc3.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/lc3.jpg
toc: false
mathjax: false
summary:
tags: 
categories: 其他
---
### Git代理
开了VPN以后发现执行 `git clone` 还是不够快，经大佬指点发现还需要配置 *git* 的代理。


![](http://img.ginta.top/markdownx/2020/03/31/a4c201b6-9795-4e65-9c45-61c446acd63a.png)


https://gist.github.com/evantoli/f8c23a37eb3558ab8765

git config --global http.proxy http://127.0.0.1:1087