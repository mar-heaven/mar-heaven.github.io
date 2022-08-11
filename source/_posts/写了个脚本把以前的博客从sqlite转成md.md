---
title: 写了个脚本把以前的博客从sqlite转成md
date: 2021-07-08 00:46:47
author: Ginta
img: /medias/banner/god.jpg
top: false
hide: false
cover: false
coverImg: /medias/banner/god.jpg
toc: false
mathjax: false
summary:
categories: 生活
---

## 前言
以前的博客是用 *django* 写的，现在要迁移到 *hexo* 了，于是乎简单粗暴的写了个脚本把 *sqlite3* 数据转换成了文件。
有几点需要改进
1. 脚本暴力过滤了所有异常数据，虽然没有一个是异常的
2. 封面图全部是一样的，其实可以随机生成的
3. 文章只生成了分类，其实tags也可以生成的

```python
import datetime
import sqlite3
conn = sqlite3.connect('db.sqlite3')
print(conn)
cur = conn.cursor()
CATEGORY_MAP = {

}

template = """---
title: {}
date: {}
author: Ginta
img: /medias/images/mingfei.jpg
top: false
hide: false
cover: false
coverImg: /medias/images/mingfei.jpg
toc: false
mathjax: false
summary:
categories: {}
---
"""

sql = "SELECT * FROM blog_category"
categories = cur.execute(sql)
for category in categories:
    category_id = category[0]
    category_title = category[3]
    CATEGORY_MAP[str(category_id)] = category_title

print(CATEGORY_MAP)

sql = "SELECT * FROM blog_post"
res = cur.execute(sql)
for post in res:
    date = post[2]
    create_date = datetime.datetime.fromisoformat(date).strftime("%Y-%m-%d %H:%M:%S")
    post_category = post[-4]
    title = post[3]
    content = post[4]
    head = template.format(title, create_date, CATEGORY_MAP[str(post_category)])
    try:
        f = open(title+ '.md', 'w', encoding="utf-8")
        f.write(head+content)
        f.close()
    except:
        print(title)
```