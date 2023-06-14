---
title: Linux 文件隐藏属性
date: 2020-02-21 01:52:03
author: Ginta
img: http://img.ginta.top/dm3.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/dm3.jpg
toc: false
mathjax: false
summary:
tags: 
categories: Linux
published: false
---
## 前言

我们都知道 **Linux** 系统文件都有 r(read)/w(write)/x(execute) 三个属性，但是文件系统还提供了隐藏属性，这些隐藏属性非常实用，可以进一步起到对文件的保护作用。



### chattr(配置文件隐藏属性)

配置文件隐藏属性的指令是 `chattr [+- - =][ASacdistu]  文件或目录名`

其中选项和参数如下:



选项与参数：



- \+ ：增加某一个特殊参数，其他原本存在参数则不动。

- \- ：移除某一个特殊参数，其他原本存在参数则不动。

- = ：设定一定，且仅有后面接的参数

- A ：当设定了 A 这个属性时，若你有存取此文件(或目录)时，他的访问时间 atime 将不会被修改，

可避免 I/O 较慢的机器过度的存取磁盘。(目前建议使用文件系统挂载参数处理这个项目)

- S ：一般文件是异步写入磁盘的(原理请参考前一章 sync 的说明)，如果加上 S 这个属性时，

当你进行任何文件的修改，该更动会『同步』写入磁盘中。

- a ：**当设定 a 之后，这个文件将只能增加数据，而不能删除也不能修改数据，只有 root 才能设定这属性**

- c ：这个属性设定之后，将会自动的将此文件『压缩』，在读取的时候将会自动解压缩，

但是在储存的时候，将会先进行压缩后再储存(看来对于大文件似乎蛮有用的！)

- d ：当 dump 程序被执行的时候，设定 d 属性将可使该文件(或目录)不会被 dump 备份

- i ：**这个 i 可就很厉害了！他可以让一个文件『不能被删除、改名、设定连结也无法写入或新增数据！』

对于系统安全性有相当大的帮助！只有 root 能设定此属性**

- s ：当文件设定了 s 属性时，如果这个文件被删除，他将会被完全的移除出这个硬盘空间，

所以如果误删了，完全无法救回来了喔！

- u ：与 s 相反的，当使用 u 来配置文件案时，如果该文件被删除了，则数据内容其实还存在磁盘中，

可以使用来救援该文件喔！

- 注意 1：属性设定常见的是 a 与 i 的设定值，而且很多设定值必须要身为 root 才能设定

- 注意 2：xfs 文件系统仅支援 AadiS 而已



```

admin@iZwz93u7y9mplneahfm5doZ:~$ cd /tmp/

admin@iZwz93u7y9mplneahfm5doZ:/tmp$ touch attrtest

admin@iZwz93u7y9mplneahfm5doZ:/tmp$ chattr +i attrtest 

chattr: Operation not permitted while setting flags on attrtest

admin@iZwz93u7y9mplneahfm5doZ:/tmp$ sudo chattr +i attrtest 

admin@iZwz93u7y9mplneahfm5doZ:/tmp$ sudo rm attrtest   <=此时sudo也就是root都无法删除了

rm: cannot remove 'attrtest': Operation not permitted

admin@iZwz93u7y9mplneahfm5doZ:/tmp$ chattr -i attrtest 

chattr: Operation not permitted while setting flags on attrtest

admin@iZwz93u7y9mplneahfm5doZ:/tmp$ sudo chattr -i attrtest  <=把i属性取消掉就可以删除了

admin@iZwz93u7y9mplneahfm5doZ:/tmp$ rm attrtest```



其中最常用的就是 **i** 和 **a** 属性了，**i** 让一个文件无法修改，无法被删除，也不能被软链接，对系统安全性有很重要的意义。**a** 让一个文件只能增加数据，无法修改和删除数据。

		

### lsattr(显示文件隐藏属性)

显示隐藏属性的指令如下： `lsattr [- adR]  文件 或者 目录`

选项与参数:



- \-a ：将隐藏文件的属性也秀出来

- \-d ：如果接的是目录，仅列出目录本身的属性而非目录内的文件名

- \-R ：连同子目录的数据也一并列出来