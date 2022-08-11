---
title: Python 线程池 ThreadPoolExecutor
date: 2019-12-20 04:31:05
author: Ginta
img: http://img.ginta.top/fantasy2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/fantasy2.jpg
toc: false
mathjax: false
summary:
tags: 
  - 多线程
categories: python
---
## 线程池
以前我们定义多线程任务的时候都是通过循环来控制线程数量，很不优雅：
```
import threading


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(self.name)

if __name__ == "__main__":

    t_list = []
    for i in range(4):
        name = "线程-" + str(i)
        t = MyThread(i, name, i)
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
```
这样做当然也是可以的，不过一方面是代码有些难看，虽然逻辑上是清晰的，另外一方面是我们无法知道哪个线程完成了，而且控制并发的方式也仅限于给循环的变量不同，说白了还是看起来不舒服。

### 目标
我们要寻求一种方式既可以实现多线程的效果，让代码看起来优雅一点。而且程序还可以知道哪些任务完成了

### 线程池
*Python3* 的线程池是在 **concurrent** 包下的 **ThreadPoolExecutor** 来实现的
现在我们写一个简单的线程池例子
```
from concurrent.futures import ThreadPoolExecutor,
def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times
    
executor = ThreadPoolExecutor(max_workers=32)
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))
task3 = executor.submit(get_html, (3))
```
如果我们想知道哪个任务执行完没有，可以用到 *done()* 方法
>task1.done()
>
返回是 *True* 说明执行完了， *False* 说明没有执行完 

在任务 **还未开始** 的时候我们可以使用 *cancel* 方法取消，如：`task2.cancel()`

通过 *submit()* 函数提交执行的函数到线程池中, 是立即返回，也就是说主线程还是在向下进行的。*max_workers* 参数是控制同时执行的最大任务数，这里我们有三个任务，但是最大任务数为 2。*submit* 有两个参数，一个就是所要执行的函数，**一定不能加括号**，另一个就是函数参数，**这里哪怕只有一个参数也要像我这样括起来，不然会出问题！**。由于*max_workers*  是2，一开始有两个在执行，如果有一个先执行完毕了，第三个任务才会开始执行。比起之前的 *for*  循环要好看不少。

如果有N个任务我们肯定不能一个个定义，用列表生成式就可以：
```
# ... 其他代码
def get_html(url):
    time.sleep(times)
    print("get page {} success".format(times))
    return times
executor = ThreadPoolExecutor(max_workers=2)
urls = [3,2,4]
all_task = [executor.submit(get_html, (url) ) for url in urls]
```

### 高级
我们想看看有多少个任务完成了，可以用 *concurrent.futures* 里的 *as_completed(task)* 方法，有一个参数可以是单独的 *task* 或者一个列表：
```
# ... 其他代码
all_task = [executor.submit(get_html, (url) ) for url in urls]

for future in as_completed(all_task):
    data = future.result()
    print("get {} page".format(data))
```
我们的 *task* 返回值在 *future.result()* 中 *as_completed* 在遍历的时候如果有函数执行完了就会返回执行完的结果，以后的任务执行完一个这里就会返回一个，可以理解为 *as_completed* 会等待任务执行，比如我们这里在遍历的时候只有一个执行完了，那就只会打印一个，如果有第二个执行完了，它就会打印第二个，而且这个也不会影响到主线程。

### 等待
如果我们想计算一下整个项目执行的时间，但是线程池不会阻塞主线程，就无法实现。
```
# ... 其他代码

start = time.time()
all_task = [executor.submit(get_html, (url)) for url in urls]
print("all tasks have done,used {}s".format(time.time()-start))
```
>all tasks have done,used 0.0010027885437011719s
get page 2 success
get page 3 success
get page 4 success

可以看到，任务开始以后主线程继续执行了，所以才会看到主线程的打印。

不过 *concurrent.futures*  给我们提供了一个 *wait()* 方法，可以让我们等待一个任务执行完，否则一直阻塞在当前位置，当然他也可以传一个列表：
```
start = time.time()
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task)
print("all tasks have done")
```
>get page 2 success
get page 3 success
get page 4 success
all tasks have done,used 6.002103328704834s

可以看到，这里就会等待所有任务执行完主线程才会继续，至于为什么打印的是 *6s* 而不是最长线程所用的 *4s*，是因为我们前面设置了 `executor = ThreadPoolExecutor(max_workers=2)`，限制了它最大的并发数，也就是说 *2s* 后才会执行第三个任务所以用时就是 *2s + 4s = 6s*。