---
title: django-allauth 阿里云发送邮件出现nginx 504解决方法
date: 2019-11-28 07:08:09
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
  - Django
  - 邮件
categories: Django
---
## 前言
在博客的认证中使用到了 `django-allauth` 模块进行用户注册登录，但是在注册环节配置邮箱系统的时候出了问题，搞了好几个小时终于解决了
原来我的配置如下
首先是github配置：
```
Homepage URL:
http://ginta.top/
Authorization callback URL:
http://ginta.top/accounts/github/login/callback/
```

这是`settings.py` *django-allauth* 配置
```
# django-allauth配置
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # 强制注册邮箱验证(注册成功后，会发送一封验证邮件，用户必须验证邮箱后，才能登陆)
ACCOUNT_AUTHENTICATION_METHOD = "username_email"     # 登录方式(选择用户名或者邮箱都能登录)
ACCOUNT_EMAIL_REQUIRED = True           # 设置用户注册的时候必须填写邮箱地址
ACCOUNT_LOGOUT_ON_GET = False           # 用户登出(需要确认)
# smtp 服务器地址
EMAIL_HOST = "smtp.qq.com"
# 默认端口25，若请求超时可尝试465
EMAIL_PORT = 25
# 用户名
EMAIL_HOST_USER = ".....@qq.com"
# 邮箱代理授权码（不是邮箱密码）
EMAIL_HOST_PASSWORD = "******"

# 发送人
EMAIL_FROM = ".....@qq.com" #
# 默认显示的发送人，（邮箱地址必须与发送人一致），不设置的话django默认使用的webmaster@localhost
DEFAULT_FROM_EMAIL = ".....@qq.com"
```

线下测试的时候没有问题，邮件也能发送，但是发布到阿里云上就是不行，一直出现邮件超时，也就是 *nginx 504* 的情况，网上有说把 *nginx* 超时时间改一下，我没尝试，一方面是因为默认已经是一分钟了，用户哪能等那么久，另一个是看到有说 **25端口** 在阿里云默认是关闭的，总之要进行一系列操作什么的，好在还可以用465端口，**但是只把25端口改成465端口还是出现超时状态！！** ，后来有看到有加上一句 `EMAIL_USE_SSL = True`，于是试了一下，解决了。最后附上完整配置, *github* 配置不变，只改 *settings.py* 就好 ：

```
# django-allauth配置
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # 强制注册邮箱验证(注册成功后，会发送一封验证邮件，用户必须验证邮箱后，才能登陆)
ACCOUNT_AUTHENTICATION_METHOD = "username_email"     # 登录方式(选择用户名或者邮箱都能登录)
ACCOUNT_EMAIL_REQUIRED = True           # 设置用户注册的时候必须填写邮箱地址
ACCOUNT_LOGOUT_ON_GET = False  # 用户登出(需要确认)
SOCIALACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# smtp 服务器地址
EMAIL_HOST = "smtp.qq.com"
# 默认端口25，若请求超时可尝试465
EMAIL_PORT = 465
EMAIL_USE_SSL = True
# 用户名
EMAIL_HOST_USER = "***@qq.com"
# 邮箱代理授权码（不是邮箱密码）
EMAIL_HOST_PASSWORD = "****"
# 发送人
EMAIL_FROM = "***@qq.com" #
# 默认显示的发送人，（邮箱地址必须与发送人一致），不设置的话django默认使用的webmaster@localhost
DEFAULT_FROM_EMAIL = "***@qq.com"
```