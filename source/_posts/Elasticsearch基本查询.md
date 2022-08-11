---
title: Elasticsearch基本查询
date: 2019-12-28 14:26:20
author: Ginta
img: http://img.ginta.top/qinshi2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/qinshi2.jpg
toc: false
mathjax: false
summary:
tags: 
categories: 数据库
---
### 准备数据
```
# 添加映射  
PUT lagou
{
  "mappings": {
    "job":{
      "properties": {
        "title":{
          "store": true,
          "type": "text",
          "analyzer": "ik_max_word"
        },
        "company_name":{
          "store": true,
          "type": "keyword"
        },
        "desc":{
          "type": "text"
        },
        "comments":{
          "type": "integer"
        },
        "add_time":{
          "type": "date",
          "format": "yyyy-MM-dd"
        }
      }
    }
  }
}

POST lagou/job/
{
    "title":"python django 开发工程师",
    "company_name":"美团科技有限公司",
    "desc":"对django的概念熟悉，熟悉python基础知识",
    "comments":20,
    "add_time":"2019-5-30"
}

POST lagou/job/
{
    "title":"python scrapy redis分布式爬虫基本",
    "company_name":"百度科技有限公司",
    "desc":"scrapy的概念熟悉，熟悉redis基础知识",
    "comments":5,
    "add_time":"2019-5-1"
}

POST lagou/job/
{
    "title":"elasticsearch打造搜索引擎",
    "company_name":"阿里巴巴科技有限公司",
    "desc":"熟悉数据结构算法，熟悉python基础开发",
    "comments":60,
    "add_time":"2019-4-15"
}

POST lagou/job/
{
    "title":"python打造推荐引擎系统",
    "company_name":"阿里巴巴科技有限公司",
    "desc":"熟悉推荐引擎的原理以及算法，掌握C语言",
    "comments":60,
    "add_time":"2019-1-22"
}

```

## 查询
### 基本查询
1. match(会对输入进行分词)
```
GET lagou/_search
{
  "query": {
    "match": {
      "title": "爬取"
    }
  }
}

GET lagou/_search
{
  "query": {
    "match": {
      "title": "爬取"
    }
  }
}
```

2. term(不会分词)
```
GET lagou/_search
{
  "query": {
    "term": {
      "title": "python爬虫"
    }
  }
}
```

3. terms(满足任何一个)
```
# terms查询
GET lagou/_search
{
  "query": {
    "terms": {
      "title": ["工程师", "django", "系统"]
    }
  }
}
```

4. query查询(控制查询的返回数量)
```
GET lagou/_search
{
  "query": {
    "match": {
      "title": "python"
    }
  },
  "from":1,
  "size":2
}
```

5. match_all查询
```
GET lagou/_search
{
  "query": {
    "match_all": {}
  }
}
```

6. multi_match查询
```
# 比如可以指定多个字段
# 比如查询title和desc这两个字段里面包含python的关键词文档
# 可以设置权重
GET lagou/_search
{
  "query": {
    "multi_match": {
      "query": "python",
      "fields": ["title^3", "desc"]
    }
  }
}
```

7. stored_fields指定返回的字段(mappings设置了store的)
```
GET lagou/_search
{
  "stored_fields": ["title"],
  "query": {
    "match": {
      "title": "python"
    }
  }
}
```

8. sort(排序返回 asc,desc)
```
GET lagou/_search
{
  "query": {
    "match_all": {}
  },
  "sort": [
    {
      "comments": {
        "order": "desc"
      }
    }
  ]
}
```

9. range(范围查询)
boost: 权重
```
GET lagou/_search
{
  "query": {
    "range": {
      "comments": {
        "gte": 10,
        "lte": 20,
        "boost": 2.0
      }
    }
  }
}

GET lagou/_search
{
  "query": {
    "range": {
      "add_time": {
        "gt": "2019-4-1"
      }
    }
  }
}

```

10. match_phrase(短语查询，自动分词，满足所有则返回)
slop: 两个词之前的距离
```
GET lagou/_search
{
  "query": {
    "match_phrase": {
      "title": {
        "query": "python系统",
        "slop": 6
      }
    }
  }
}
```