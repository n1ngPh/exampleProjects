## 项目简介
这是一个包含多个爬虫项目的仓库，用于展示使用不同技术栈开发的爬虫，除此还有一些过验证码项目。
每个项目都有result截图，不过为防止代码滥用，部分项目删除一些js代码和请求头信息，无法直接运行。

## 项目列表
- [链家网租房信息爬虫](https://github.com/n1ngPh/exampleProjects/tree/main/lianjia)
- [汽车之家配置信息爬虫](https://github.com/n1ngPh/exampleProjects/tree/main/qicheHome)
- [智慧树模拟登录](https://github.com/n1ngPh/exampleProjects/tree/main/zhihuishu)
- [过安居客验证码](https://github.com/n1ngPh/exampleProjects/tree/main/anjuke)
- [过极验验证码](https://github.com/n1ngPh/exampleProjects/tree/main/jiyan)
- [云服务部署脚本](https://github.com/n1ngPh/exampleProjects/tree/main/healthSubmit)
- [电影搜索系统](https://github.com/n1ngPh/exampleProjects/tree/main/L805)
- [数据爬取与数据分析](https://github.com/n1ngPh/exampleProjects/tree/main/c579)

## 1. 链家网租房信息爬虫

**技术栈**: Scrapy框架、aiohttp异步、request库、Xpath、MySQL

使用三种不同的方法爬取链家网的租房信息，并将数据保存到MySQL数据库。

使用方法：
  1、运行get_url_list.py,获取需要的价格范围
  2、开启MySQL服务，运行create_table.py，创建数据表
  3、进入lianjia_ordinary或者lianjiaSpiderw文件夹进行相应的运行

## 2. 汽车之家配置信息爬虫

**技术栈**: CSS样式反爬、js文件动态加载、requests库、execjs库、re库

用于爬取汽车之家的配置信息。由于目标网站使用了CSS样式反爬和动态加载的机制，需要采取相应的反爬策略。项目使用requests库发送HTTP请求，通过execjs库模拟JavaScript的执行过程，并使用正则表达式替换字体，最终实现完整的汽车配置信息的爬取。

## 3. 智慧树模拟登录

**技术栈**: webpack改写、RSA加密、XHR断点调试、execjs库、302重定向

项目主要是Python实现WebSocket协议爬虫。通过分析智慧树客户端与服务端的通信信息，建立WebSocket连接，并获取相关参数进行登录。
使用方法：
1、下载知到APP
2、运行zhihuishu.py
3、app扫描生成的二维码

## 4. 过安居客验证码

**技术栈**: AES加密、OB混淆、OpenCV库、轨迹处理

该项目实现了对安居客滑动验证码的识别和破解。

## 5. 过极验验证码

**技术栈**: Express、AES、RSA加密、混淆、生成轨迹、staticmethod静态方法

实现了对极验三代滑块验证码的破解。通过逆向解析验证码生成的逻辑，使用Express框架传递和解密参数。还原背景图片乱序和生成滑动轨迹的加密方法，并模拟滑动轨迹的生成。

## 6. 云服务部署脚本

**技术栈**: 请求头伪装、requests、json、Linux操作

部署到云服务器上，每日模拟发包，同时通过调用企业微信API接口，可以实现日志反馈，方便查看脚本运行状况。

## 7. 电影搜索系统

**技术栈**: HTML、CSS、Flash框架、MySQL、pyecharts、requests、Xpath

该项目使用Python编程语言实现了一个电影搜索系统。通过爬取豆瓣电影信息，并将数据存储到MySQL数据库中。使用Flask框架搭建了一个本地服务器，前端界面展示电影列表，并提供搜索功能。后端实时爬取电影详情信息，并利用pyecharts库生成图表，实现在Web界面上的图表展示。

## 7. 网页数据爬取和数据分析

**技术栈**:pandas、numpy、NLTK、matplotlib、XPath、CSS、BeautifulSoup等

项目简介：此项目类似大作业，有四个任务。任务一：获取所有链接，包括子链接的子链接；任务二：从页面中提取单词，包括删除停用词，提取单词词干等等；任务三：利用任务二提取程序，爬取所有链接，生成模型；任务四：降维，绘制权重最高的标记图。

难点在于网页有各种陷阱和各种规则，比如特殊字符串了，还有一下标签不能爬，如何规范提取单词词干等等，爬取数据内容要格外小心。
