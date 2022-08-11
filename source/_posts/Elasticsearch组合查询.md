---
title: Elasticsearch组合查询
date: 2019-12-28 14:26:45
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
categories: 数据库
---
### 准备数据
```
POST lagou/testjob/_bulk
{"index":{"_id":1}}
{"salary":10, "title": "Python"}
{"index":{"_id":2}}
{"salary":20, "title": "Scrapy"}
{"index":{"_id":3}}
{"salary":30, "title": "Django"}
{"index":{"_id":4}}
{"salary":40, "title": "Elasticsearch"}
```
## 组合查询
### bool查询
>用 bool 包括 must should must_not filter 来完成，
格式如下
- filter 过渡字段
- must 所有都要有
- should 满足一个或多个
- must_not 一个都不能满足
```
bool: {
    "filter": [],
    "must": [],
    "should": [],
    "must_not"
}
```

1. filter查询
```

select * from testjob where salary=20
薪资为20k的工作
GET lagou/testjob/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all":{}
      },
      "filter": {
        "term": {
          "salary": "20"
        }
      }
    }
  }
}

# 多个
GET lagou/testjob/_search
{
  "query": {
    "bool": {
      "filter": {
        "terms": {
          "salary": ["10", "20"]
        }
      }
    }
  }
}


# select * from testjob where title="Python"
# text字段会先分词，再全部转为小写入库
# term不会预处理，直接大写查询，但是倒排索引已经全部小写了
# 所以查不到，要不就用小写，要不就用match
GET lagou/testjob/_search
{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "title":"Python"
        }
      }
    }
  }
}
```

### bool组合过滤查询
```
# 查询薪资等于20k或者工作为Python的工作，排除价格为30k的
# select * from testjob where (salary=20 OR title="Python") AND (salary !=30)
GET lagou/testjob/_search
{
  "query": {
    "bool": {
      "should":[ 
        {"term": {"salary":20}},
        {"term":{"title":"python"}}
      ],
      "must_not": [
        {"term":{"salary":30}},
        {"term":{"salary":10}}
      ]
    }
  }
}

# 嵌套查询
# select * from testjob where title="python" or (title="django" AND salary=40)
GET lagou/testjob/_search
{
  "query": {
    "bool": {
      "should":[ 
        {"term": {"title":"python"}},
        {"bool":{
          "must": [
            {"term": {"title":"elasticsearch"}},
            {"term": {"salary": 40}}
          ]}
        }
      ]
    }
  }
}
```

### 过滤空和非空
```

# 建立测试数据
POST lagou/testjob2/_bulk
{"index":{"_id":"1"}}
{"tags":["search"]}
{"index":{"_id":"2"}}
{"tags":["search", "python"]}
{"index":{"_id":"3"}}
{"orther_field":["some data"]}
{"index":{"_id":"4"}}
{"tags":null}
{"index":{"_id":"5"}}
{"tags":["search", null]}
```

```
# 处理非空值的方法
# select tags from testjob2 where tags is not NULL
GET lagou/testjob2/_search
{
  "query": {
    "bool": {
      "filter": {
        "exists": {
          "field": "tags"
        }
      }
    }
  }
}
```