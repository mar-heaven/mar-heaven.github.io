---
title: Django 使用 logging 模块的一次记录
date: 2019-11-27 02:03:20
author: Ginta
img: http://img.ginta.top/sky1.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/sky1.jpg
toc: false
mathjax: false
summary:
tags: 
  - python
  - Django
categories: Django
published: false
---
## 起因

偶尔浏览 [Stack overflow](https://stackoverflow.com/) 看到有人提出的关于日志记录的问题，比较感兴趣就尝试了一下，问题截图如下:

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191030170258391.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191030170206321.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191030170226488.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MDY4OTMz,size_16,color_FFFFFF,t_70)

意思是他想把不同的日志等级分别记录在不同的文件中，比如 *INFO* 和 *ERROR* 分别记录到 *info.log* 以及 *error.log* 文件中，然而经过上图的尝试发现只有 *ERROR* 级别的错误记录到 *error.log* 的文件中了，而 *INFO* 级别的却没有记录，有一条解答算是比较清晰的 **In your settings you have two entries for django, and django is writing logs based on the last entry.** 意思是： **当你设置两个 *django*  的 *loggers*，那么默认会执行最后一个，也就是倒数第二章图的这部分有效

```python

 'django': {

     'handlers': ['file.ERROR'],

     'level': 'ERROR',

     'propagate': True,

 },

```

解决办法也同样给出了：

```python

'loggers': {

        'django.request': {

            'handlers': ['file.DEBUG'],

            'level': 'DEBUG',

            'propagate': True,

        },

        'django': {

            'handlers': ['file.INFO', 'file.ERROR'],  # <-- Here

            'level': 'INFO',

            'propagate': True,

        }

}

```

本着 **实践是检验真理的唯一标准** ，忍不住写了个小的demo试了一下：

```python

# views.py

class IndexView(View):

    def get(self, request):

        log.info('info log file')

        log.error('error log file')



        return HttpResponse('return')



```

```python

# settings.py

'handlers': {

    'info.file': {

        'level': 'INFO',

        'class': 'logging.handlers.RotatingFileHandler',

        # 日志位置,日志文件名,日志保存目录必须手动创建

        'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/info.log"),

        # 日志格式:详细格式

        'formatter': 'verbose'

    },

    'error.file': {

        'level': 'ERROR',

        'class': 'logging.handlers.RotatingFileHandler',

        # 日志位置,日志文件名,日志保存目录必须手动创建

        'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/error.log"),

        # 日志格式:详细格式

        'formatter': 'verbose',

    },

},





# 日志对象，第一次

'loggers': {

    'django': {

        'handlers': ['info.file'],

        'propagate': False,  # 是否让日志信息继续冒泡给其他的日志处理系统

        'level': 'INFO',

    },

    'django': {

        'handlers': ['error.file'],

        'propagate': False,  # 是否让日志信息继续冒泡给其他的日志处理系统

        'level': 'ERROR',

    },

}

```

第一次的结果就是，*level* 为 *INFO* 的 *loggers* 没有记录，也就是只记录了 *error* 的日志

```python

# 日志对象，第二次

'loggers': {

    'django': {

        'handlers': ['error.file'],

        'propagate': False,  # 是否让日志信息继续冒泡给其他的日志处理系统

        'level': 'ERROR',

    },

    'django': {

        'handlers': ['info.file'],

        'propagate': False,  # 是否让日志信息继续冒泡给其他的日志处理系统

        'level': 'INFO',

    },

}

```

第二次结果相反，只有 *info.log* 文件中保存有记录。说明回答问题的这位还是很负责的！

最后测试了一下正确的方式：

```python

'loggers': {

    'django': {

        'handlers': ['info.file', 'error.file'],

        'propagate': False,  # 是否让日志信息继续冒泡给其他的日志处理系统

        'level': 'INFO',

    },

}

```

最终结果是 *INFO* 级别以及比它更低级别的日志都记录到了 *info.log* 中，就是说 *error* 等级别也一块进去了，而 *error* 以及比他更低级别的日志会记录到 *error.log* 文件中，也就是说 *error* 以及比它低级别的日志会保存两份。这符合 **logging** 库的说明。



## 后记

虽然找到了问题所在，不过提问者貌似想把不同级别的分别存储到一个文件中，就是 *info.log* 只保存 *INFO* 级别的日志，而不会保留 *error* 的日志。虽然这种需求不是很常见，毕竟 *ERROR* 以下级别的日志同样重要，也许有的公司人员比较充足，可以分2个人来分别解决 *ERROR* 以及 *CRITICAL*(严重错误，比如项目根本无法启动)也说不定~