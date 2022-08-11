---
title: Git 更新fork代码的内容
date: 2020-05-09 08:36:50
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
categories: Git/Github
---
## 前言
公司有个开源项目需要维护，之前在校的时候和同学开发一个项目双方都是admin权限可以直接 *push* 到主分支，但一般来说新的代码还是通过 *pr* 的方式提交比较稳妥。现在遇到的问题是：这次我 *pr* 了以后，下次又改动代码 *pr* 的时候就要兼顾 *fork* 源的代码有没有更新，
如果更新了这边不 *pull* 下来直接提交会引起冲突。以往的操作是如果 *fork* 源更新了代码，我就把自己仓库删掉重新 *fork* 一次。。。一次两次还好，后来无法忍受这种低能操作了，决定重新做人。

## 步骤
其实解决这个问题很简单，只需要几个步骤即可：
就拿我现在维护的项目来说 项目的地址是 [rqalpha](git@github.com:ricequant/rqalpha.git) , 我 *fork* 以后的地址是 [mar-heaven/rqalpha](https://github.com/mar-heaven/rqalpha)。

这时我在本地的 *develop* 分支改好代码准备提交，但是发现和  [rqalpha](git@github.com:ricequant/rqalpha.git) 的 *develop* 分支是冲突的，因为在此期间又有了新的 *commit*。
先看一下 *remote*
```
(base) tangxinyingdeiMac:rqalpha xinglitao$ git remote -v
origin  https://github.com/mar-heaven/rqalpha.git (fetch)
origin  https://github.com/mar-heaven/rqalpha.git (push)
```
执行  `git remote add upstream git@github.com:ricequant/rqalpha.git`
再看一下
```
(base) tangxinyingdeiMac:rqalpha xinglitao$ git remote -v
origin  https://github.com/mar-heaven/rqalpha.git (fetch)
origin  https://github.com/mar-heaven/rqalpha.git (push)
upstream        git@github.com:ricequant/rqalpha.git (fetch)
upstream        git@github.com:ricequant/rqalpha.git (push)
```
*fetch* 一下
```
(base) tangxinyingdeiMac:rqalpha xinglitao$ git fetch upstream
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 16 (delta 10), reused 8 (delta 6), pack-reused 0
Unpacking objects: 100% (16/16), done.
From github.com:ricequant/rqalpha
 * [new branch]        0.3.x                    -> upstream/0.3.x
 * [new branch]        2.1.x                    -> upstream/2.1.x
 * [new branch]        2.2.x                    -> upstream/2.2.x
 * [new branch]        3.0.x                    -> upstream/3.0.x
 * [new branch]        3.1.1.x                  -> upstream/3.1.1.x
 * [new branch]        3.3.0.x                  -> upstream/3.3.0.x
 * [new branch]        3.3.x                    -> upstream/3.3.x
 * [new branch]        3.4.x                    -> upstream/3.4.x
 * [new branch]        develop                  -> upstream/develop
 * [new branch]        feature/broker_refactory -> upstream/feature/broker_refactory
 * [new branch]        feature/stat             -> upstream/feature/stat
 * [new branch]        master                   -> upstream/master
```

然后就可以 *merge* 了
```
(base) tangxinyingdeiMac:rqalpha xinglitao$ git merge upstream/develop
Merge made by the 'recursive' strategy.
 rqalpha/mod/rqalpha_mod_sys_progress/mod.py | 8 ++++----
 rqalpha/model/bar.py                        | 2 ++
 rqalpha/utils/log_capture.py                | 1 +
 3 files changed, 7 insertions(+), 4 deletions(-)
```

收工！