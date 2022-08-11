---
title: apscheduler
date: 2020-03-28 16:45:55
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
  - python
categories: python
---
## 引言
**apscheduler** 可以拆分成两部分：

- **aps**: 进阶生产规划及排程系统
- **scheduler**: 调度程序，日程安排程序

当程序希望某个函数每隔一段时间执行一次，或者某个函数在某天（每天）的某个时间执行，就可以引入 **apscheduler** 库。

```
from apscheduler.schedulers.blocking import BlockingScheduler
import time

def doing():
  print("do doing!!")

if __name__=="__main__":
    sched = BlockingScheduler()  # 1
    sched.add_job(doing, 'interval', seconds=10) # 2
    sched.start() # 3
```

1. 实例化 *BlockingScheduler* 对象
2. 添加任务

*add_job()* 函数4个常用参数，第一个是所要执行的函数
第二个是触发器，可以定时触发，或者间歇性触发

- date 日期：触发任务运行的具体日期
- interval 间隔：触发任务运行的时间间隔
- cron 周期：触发任务运行的周期
第三个参数是在选择触发器以后设置的，比如scconds=10就是10s执行一次
args用来给函数传参。args=['text']
3. 启动日程
可以通过sched.add_job()启动多个定时任务后再执行整个调度器
比如
```
import time
from apscheduler.schedulers.background import BackgroundScheduler
def func1():
    print("func1")

def func2():
    print("func2")

def func3():
    print("func3")


if __name__ == "__main__": 
    func_list = [func1, func2, func3] # 设置多个函数
    sched = BackgroundScheduler()
    for index, func in enumerate(func_list): 
        sched.add_job(func, 'interval', seconds=int(index)+1)
    sched.start() # 最后一次性启动
    while True:
        time.sleep(1)
        print('*'*50)
```