---
title: DRF JWT 配置
date: 2020-02-13 11:14:48
author: Ginta
img: http://img.ginta.top/lc2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/lc2.jpg
toc: false
mathjax: false
summary:
tags: 
  - Django
categories: Django
---
## 前言
原本 *github* 上有一个和 *drf* 版本对应的开源项目，最近在做项目的时候由于用的是新版本 *drf* ，特地到网上仓库看了一下之前使用的 [django-rest-framework-jwt](https://github.com/jpadilla/django-rest-framework-jwt) 已经停止维护了，幸运的是在该仓库的 *issues* 里发现了另一个持续维护的项目，[django-rest-framework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt)，目前已经支持 *django3.0*了。

## 使用
首先使用pip进行安装:
```
pip install djangorestframework-simplejwt
```

然后在 DRF 配置加入以下内容
```
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}
```

那么我们如何获取 *token* 呢？这时候需要配置一个路由来获取 *token*，直接配置到项目根目录下的 *urls.py* 里就好
```
# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```

然后就可以使用 *postman* 来测试获取token了


![](http://img.ginta.top/markdownx/2019/12/02/dc885b29-d663-49cb-9d68-3b9906e3e319.png)

之后发送请求的时候使用上面的 **access**就好，不用每次请求都输入用户名密码


![](http://img.ginta.top/markdownx/2019/12/02/0a7bb631-0a12-4cbb-8bbc-2e58c06b4251.png)

请求的方式没有太多变化，就是在请求头中多了一个 *Authorization* ，对应的值格式是 Bearer+一个空格+access。
**Bearer** 也可以改为其他的名字，这个是官方配置的值，比如我习惯用 **jwt** 开头，在项目的 *settings.py* 文件中加入如下配置
```
# settings.py
# simple_jwt config
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```
其他的参数看官方文档，这里举一个例子 *AUTH_HEADER_TYPES* 这里值为 *Bearer* 就是刚才提到 *Authorization* 开头要加的字符串，可以根据自己喜好设置。

# 补充
如果想让所有的路由都需要 jwt 认证，那么可以在 *drf* 配置中增加全局配置：
```
# DRF config
REST_FRAMEWORK = {
    # 其他内容			
    "DEFAULT_PERMISSION_CLASSES":[
        'rest_framework.permissions.IsAuthenticated'
    ]
}
```
如果有的路由，比如用户注册的时候并没有办法获取 *token* ，那么该函数就跳过登陆验证，就是说该请求并不需要在 *header* 中添加 *Authorization*，那么我们可以这样：
```
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class CreateUserView(GenericViewSet, mixins.CreateModelMixin):
    """
    用户注册
    """
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

```
把 *permission_classes* 赋值为空列表即可。