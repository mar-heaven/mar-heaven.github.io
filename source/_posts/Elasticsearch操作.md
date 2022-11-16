---
title: Elasticsearch操作
date: 2019-12-28 14:25:47
author: Ginta
img: http://img.ginta.top/chaoshou2.jpg
top: false
hide: false
cover: false
coverImg: http://img.ginta.top/chaoshou2.jpg
toc: false
mathjax: false
summary:
tags: 
categories: 数据库
---
```

# es的文档，索引的 CRUD 操作

# 索引初始化操作

# 指定分片和副本的数量

# shards一旦设置不能修改（副本数量）



# 设置索引  

PUT lagou

{

  "settings": {

    "index":{

      "number_of_shards": 5,

      "number_of_replicas": 2

    }

  }  

}



GET lagou/_settings

GET _all/_settings

GET .kibana,lagou/_settings

GET lagou/job/1/_source



# 修改settings

PUT lagou/_settings

{

  "number_of_shards": 2

}



# 保存文档  

PUT lagou/job/2

{

    "title": "python分布式爬虫开发",

    "salary_min": 15000,

    "city": "北京",

    "company": {

        "name": "百度",

        "company_addr": "北京市软件园"

    },

    "publish_data": "2019-5-30",

    "comments": 15

}



POST lagou/job/1

{

    "title": "python django 开发工程师",

    "salary_min": 3000,

    "city": "天猫",

    "company": {

        "name": "美团科技",

        "company_addr": "北京市软件园A区"

    },

    "publish_data": "2019-5-30",

    "comments": 2

}





GET lagou/job/2?_source=city,company.name



# 修改文章

PUT lagou/job/2

{

    "title": "python分布式爬虫开发",

    "salary_min": 15000,

    "city": "北京",

    "company": {

        "name": "百度",

        "company_addr": "北京市软件园"

    },

    "publish_data": "2019-5-30",

    "comments": 23

}



# 修改文章2

POST lagou/job/2/_update

{

  "doc":{

    "comments": 21

  }

}





DELETE lagou/job/1

DELETE lagou



# 批量获取

GET _mget

{

  "docs":[

    { 

      "_index":"lagou",

      "_type": "job2",

      "_id": 2

    },

    { 

      "_index":"lagou",

      "_type": "job",

      "_id": 1

    }

  ]

}



# index一样

GET lagou/_mget

{

  "docs":[

    { 

      "_type": "job2",

      "_id": 2

    },

    { 

      "_type": "job",

      "_id": 1

    }

  ]

}





# index,type一样



GET lagou/job2/_mget

{

  "docs":[

    { 

      "_id": 2

    },

    { 

      "_id": 1

    }

  ]

}



GET lagou/job2/_mget

{

  "ids": [1,2]

}





```

### bulk批量操作

bulk操作不能分行，json必需一行写完

```

{"index": {"_index": "zhilian", "_type": "job", "_id": "1"}}

{"title": "python分布式爬虫开发","salary_min": 15000,"city": "北京","company": {"name": "百度","company_addr": "北京市软件园"},"publish_data": "2019-5-30","comments": 23}

{"index": {"_index": "zhilian", "_type": "job", "_id": "2"}}

{"title": "爬虫开发","salary_min": 1500,"city": "太原","company": {"name": "阿里","company_addr": "太原市软件园"},"publish_data": "2019-5-30","comments": 23}

```



### bulk其他操作

```

{"index": {"_index": "test", "_type": "type1", "_id": "1"}}

{"field1" : "value1"}

{"delete": {"_index": "test", "_type": "type1", "_id": "2"}}

{"create": {"_index": "test", "_type": "type1", "_id": "3"}}

{"field1" : "value3"}

{"update": {"_index": "index1", "_type": "type1", "_id": "1"}}

{"doc":{"field2": "value2"}

```



### elasticsearch映射

```

# 创建索引

PUT lagou

{

  "mappings": {

    "job":{

      "properties": {

        "title":{

          "type": "text"

        },

        "salary_min":{

          "type": "integer"

        },

        "city":{

          "type":"keyword"

        },

        "company":{

          "properties": {

            "name":{

              "type":"text"

            },

            "company_addr":{

              "type":"text"

            },

            "employee_count":{

              "type":"integer"

            }

          }

        },

        "publish_date":{

          "type": "date",

          "format": "yyyy-MM-dd"

        },

        "comments":{

          "type": "integer"

        }

      }

    }

  }

}





PUT lagou/job/3

{

    "title": "python分布式爬虫开发",

    "salary_min": "abc",

    "city": "北京",

    "company": {

        "name": "百度",

        "company_addr": "北京市软件园",

        "employee_count":50

    },

    "publish_data": "2019-5-30",

    "comments": 15

}



GET lagou/_mapping/job

GET _all/_mapping/job

```