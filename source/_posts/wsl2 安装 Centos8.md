---
title: wsl2 安装 Centos8
date: 2021-07-04 11:07:37
author: Ginta
img: http://img.ginta.top/huoying2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/huoying2.jpg
toc: false
mathjax: false
summary:
tags: 
  - WSL2
categories: 其他
---
## 前言
由于开发需要安装 *centos* 版本的 *wsl*， 但 *Windows Store* 里只有 *Ubuntu*、*Debian* 等 *kernel*，好消息是 *Github* 上可以找到对应版本的安装包。

### 安装 Chocolatey
NuGet（读作New Get）是用于微软.NET开发平台的软件包管理器，是一个Visual Studio的扩展。Chocolatey 是基于 NuGet 的一个软件包管理器，就像 Linux 中的 yum 或 apt 一样，在 Windows10 中也可以用命令行安装程序了。

右键单击开始菜单，选择 Windows PowerShell(管理员)，打开一个具有管理员权限的 PowerShell 窗口，输入命令并回车：
```
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
完成后，输入命令：choco ，如果能正确显示版本号，说明安装成功。

详情请查看官网文档安装说明

### LxRunOffline 是非常实用的 WSL 管理软件，可以备份、创建、恢复、导出WSL子系统，也可以安装适配 WSL 的任何 Linux 发行版，可以将 WSL 子系统安装到任意目录中。

在 PowerShell 窗口中输入命令安装LxRunOffline，安装完成后重启 PowerShell。
```
choco install lxrunoffline -y
```
### 安装 Centos8 wsl
[打开链接](https://github.com/mishamosher/CentOS-WSL/releases/tag/8-stream-20210603)，这里直接下载 [CentOS8-stream.zip
](https://github.com/mishamosher/CentOS-WSL/releases/download/8-stream-20210603/CentOS8-stream.zip)，解压后会发现有一个 **rootfs.tar.gz** 文件，使用 ` lxrunoffline install -n CentOS -d F:/centos -f E:\CentOS8-stream\rootfs.tar.gz` 命令来安装，其中 **-d** 后面是 *kernel* 想要安装到的位置，**-f** 的参数是 **rootfs.tar.gz** 的所有路径。
然后将这个发行版设置为 **WSL2**：`wsl --set-version CentOS 2`

### 换源
由于默认源都用的国外安装路径，下载东西很慢，需要换成阿里源
1. 备份原文件
```
cd /etc/yum.repos.d
mv CentOS-Base.repo CentOS-Base.repo.bak
mv CentOS-extras.repo CentOS-extras.repo.bak
mv CentOS-centosplus.repo CentOS-centosplus.repo.bak
mv CentOS-PowerTools.repo CentOS-PowerTools.repo.bak
mv CentOS-AppStream.repo CentOS-AppStream.repo.bak
```
2.  下载
```
# wget -O CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo
vi CentOS-Stream-BaseOS.repo
```
这里有两点需要解释一下，目前安装的 *centos8* 没有内置 *wget* 和 *vim* ，不过上边只是一个文件，可以用 *windows* 下载完之后将里面的内容复制一下，然后粘贴到 **CentOS-Stream-BaseOS.repo** 保存就好。
3. 删除缓存并生成新的缓存
```
dnf clean all
dnf makecache
```

### wsl2配置使用windows网络代理
我想要在 *wsl2* 上安装 *helm* ，脚本中有需要访问外网，这就需要一个代理。不过我的 *windows* 已经有代理了，只需要让它使用 *windows* 的代理就好。

- wsl2获取win10 ip
  - cat /etc/resolv.conf|grep nameserver|awk '{print $2}' => 例如：172.20.192.1
注：由于windows防火墙的存在，此时可能出现ping 172.20.192.1失败
- 新建防火墙入站规则

  - 打开控制面板\系统和安全\Windows Defender 防火墙
  - 点击入站规则->新建规则
  - 规则类型：自定义
  - 程序：所有程序
  - 协议和端口：默认即可
  - 作用域：
    - 本地ip处选择“任何IP地址”
    - 远程ip处选择“下列IP地址”，并将wsl2的IP添加进去。（请根据自己wsl2的ip进行计算，我这里添加了172.20.192.1/20）（掩码一般是20位）
  - 操作：允许连接
  - 配置文件：三个全选
  - 名称描述：请自定义
  - 注意：这一步完成后，从wsl2 ping主机的ip应该可以ping通了。
- 防火墙配置
  - 打开控制面板\系统和安全\Windows Defender 防火墙\允许的应用。
  - 将与代理相关的应用程序均设置为：允许其进行专用、公用网络通信。
  - 特别注意的是：将Privoxy也配置为允许
  
- windows端代理软件配置
  - 启用“允许来自局域网的连接”
- 测试
  - 在wsl2中配置http代理，如export http_proxy="http://172.20.192.1:1080"。注意：端口号请结合自己的代理设置进行修改
  - 执行命令curl cip.cc查看ip地址

## 部分资料参数文章
1. [arp命令 centos 安装_WSL2子系统安装CentOS8及源码编译Nginx1.18+PHP7.4+MySql8.0开发环境...](https://blog.51cto.com/u_15057852/2567230)
2. [wsl2配置使用windows网络代理](https://blog.csdn.net/nick_young_qu/article/details/113709768)

