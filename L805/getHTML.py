# -*- coding:utf-8 -*-
# @Time : 2022/4/20 22:12
# @File : getHTML.py
# @Software : PyCharm
import gotoMySQL
from pyecharts.charts import Bar, Page, Grid
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
import datetime
import collections
from pyecharts.charts import WordCloud

"""
生成HTML页面
"""

class GetHTML1:
    # 一级界面生成
    def __init__(self):
        self.headHTML = """
            <html lang="en"><head>

            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width,initial-scale=1">
        <!--    <link rel="icon" href="https://ssr1.scrape.center/static/img/favicon.ico">-->
        <!--    url_for参考https://zhuanlan.zhihu.com/p/78778387-->
            <link rel="icon" href="{{ url_for('static', filename='/img/favicon.ico') }}">
            <title>Scrape | Movie</title>


            <link rel="stylesheet" href="{{ url_for('static', filename='/css/app.css') }}" type="text/css">
            <link rel="stylesheet" href="{{ url_for('static', filename='/css/index.css') }}" type="text/css">

        </head>
        <body>
        <div id="app">
            <div data-v-74e8b908="" class="el-row" id="header">
                <div data-v-74e8b908="" class="container el-col el-col-18 el-col-offset-3">
                    <div data-v-74e8b908="" class="el-row">
                        <div data-v-74e8b908="" class="logo el-col el-col-4">
                            <a data-v-74e8b908="" href="/" class="router-link-exact-active router-link-active">
                                <img data-v-74e8b908="" src="{{ url_for('static', filename='/img/logo.png') }}" class="logo-image">
                                <span data-v-74e8b908="" class="logo-title">Scrape</span>
                            </a>
                        </div>
                    </div>
                </div>
                <div style="float: right; padding-right:100px">
                <form method="POST" action="/name" class="el-button category el-button--primary el-button--mini" >
                    <input type="text" placeholder="请输入查询的电影" name="keyword" class="el-button category el-button--primary el-button--mini"  />
                    <input type="submit" class="el-button category el-button--primary el-button--mini" value="查询">
                </form>
            </div>
            </div>

            """
        self.endHTML = """"""
        self.MoviesHTML = """"""
        self.page = 1

    # 合成MoviesHTML
    def main(self, data):
        token = data[1]
        img = data[6]
        title = data[2]
        pingfen = data[3]
        comment = data[4]
        arr = data[7]

        pageHTML = """"""
        for i in range(1, 11):
            if i == self.page:
                pageHTML += f"""
                <li class="number active">
                                    <a href="/page/{i}">{i}</a>
                                </li>\n
                """
            else:
                pageHTML += f"""
                <li class="number">
                                    <a href="/page/{i}">{i}</a>
                                </li>\n
                """
        # 利用%修改字符串中的%s
        self.endHTML = """
        <div class="el-loading-mask" style="display: none;">
                    <div class="el-loading-spinner">
                        <svg viewBox="25 25 50 50" class="circular">
                            <circle cx="50" cy="50" r="20" fill="none" class="path"></circle>
                        </svg>
                    </div>
                </div>
            </div>
            <div data-v-7f856186="" class="el-row">
                <div data-v-7f856186="" class="el-col el-col-10 el-col-offset-11">
                    <div data-v-7f856186="" class="pagination m-v-lg">
                        <div data-v-7f856186="" class="el-pagination is-background">
                            <span class="el-pagination__total">共 100 条</span>

                            <button type="button" disabled="disabled" class="btn-prev">
                                <i class="el-icon el-icon-arrow-left"></i>
                            </button>

                            <ul class="el-pager">


                                %s


                            </ul>

                            <a href="/page/%s" class="next">
                                <button type="button" class="btn-next"><i class="el-icon el-icon-arrow-right"></i></button>
                            </a>

                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
    </body></html>
        """ % (pageHTML, self.page+1)

        oneMovieHTML = """
        <div data-v-7f856186="" class="el-card item m-t is-hover-shadow">
                        <div class="el-card__body">
                            <div data-v-7f856186="" class="el-row">
                                <div data-v-7f856186="" class="el-col el-col-24 el-col-xs-8 el-col-sm-6 el-col-md-4">
                                    <a data-v-7f856186="" href="/token/%s" class="">
                                        <img data-v-7f856186="" src="{{ url_for('static', filename='/img/%s') }}" class="cover">
                                    </a>
                                </div>
                                <div data-v-7f856186="" class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16">
                                    <a data-v-7f856186="" href="/token/%s" class="name">
                                        <h2 data-v-7f856186="" class="m-b-sm">%s</h2>
                                    </a>
                                    <div data-v-7f856186="" class="categories">

                                        <button data-v-7f856186="" type="button" class="el-button category el-button--primary el-button--mini">
                                            <span>%s</span>
                                        </button>
                                    </div>
                                    <div data-v-7f856186="" class="m-v-sm info">
                                        <span data-v-7f856186="">%s</span>
                                    </div>
                                </div>
                                <div data-v-7f856186="" class="el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4">
                                    <p data-v-7f856186="" class="score m-t-md m-b-n-sm">
                                        %s</p>
                                    <p data-v-7f856186="">
                                    </p><div data-v-7f856186="" role="slider" aria-valuenow="4.75" aria-valuetext="" aria-valuemin="0" aria-valuemax="5" tabindex="0" class="el-rate">


                                </div>
                                    <p></p></div>
                            </div>
                        </div>
                    </div>
                </div>\n
        """

        self.MoviesHTML += oneMovieHTML % (token, img.split('/')[-1], token, title, arr, comment, pingfen)

    # 生成一页
    def savePage(self):
        html = self.headHTML + self.MoviesHTML + self.endHTML
        with open(f"templates/page{self.page}.html", "w", encoding="utf-8") as f:
            f.write(html)
            self.page += 1
            # 初始化，为下页准备
        self.MoviesHTML = """"""

    def saveHTML1(self):
        num = 0
        # 获取mysql数据
        mysql = gotoMySQL.GotoMySQL(0)
        mysqlAllData = mysql.readMysql()
        for row in mysqlAllData:
            num += 1
            if num == 10:
                num = 0
                self.savePage()
            self.main(row)
        mysql.close()

class GetHTML2:
    # 二级界面生成
    def __init__(self):
        pass
    def saveHTML2(self, data):
        html2 = """
        <html lang="en">
<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="icon" href="/static/img/favicon.ico">
  <title>Scrape | Movie</title>


  <link href="/static/css/app.css" type="text/css" rel="stylesheet">

<link href="/static/css/detail.css" type="text/css" rel="stylesheet">

</head>
<body>
<div id="app">
  <div data-v-74e8b908="" class="el-row" id="header">
    <div data-v-74e8b908="" class="container el-col el-col-18 el-col-offset-3">
      <div data-v-74e8b908="" class="el-row">
        <div data-v-74e8b908="" class="logo el-col el-col-4">
          <a data-v-74e8b908="" href="/" class="router-link-exact-active router-link-active">
            <img data-v-74e8b908="" src="/static/img/logo.png" class="logo-image">
            <span data-v-74e8b908="" class="logo-title">Scrape</span>
          </a>
        </div>
      </div>
    </div>
  </div>

<div data-v-63864230="" id="detail" class="m-t">
  <div data-v-63864230="" class="el-row">
    <div data-v-63864230="" class="el-col el-col-18 el-col-offset-3">
      <div data-v-63864230="" class="el-card is-hover-shadow"><!---->
        <div class="el-card__body">
          <div data-v-63864230="" class="item el-row">
            <div data-v-63864230="" class="el-col el-col-24 el-col-xs-0 el-col-sm-8">
              <a data-v-63864230="" class="router-link-exact-active router-link-active">
                <img
                    data-v-63864230=""
                    src="{{ url_for('static', filename='/img/%s') }}"
                    class="cover">
              </a>
            </div>
            <div data-v-63864230="" class="p-h el-col el-col-24 el-col-xs-16 el-col-sm-12">
              <a data-v-63864230=""
                 class="router-link-exact-active router-link-active">
                <h2 data-v-63864230="" class="m-b-sm">%s</h2></a>
              <div data-v-63864230="" class="categories">

                <button data-v-7f856186="" type="button"
                        class="el-button category el-button--primary el-button--mini">
                  <span>%s</span>
                </button>
              </div>
              <div data-v-63864230="" class="drama"><h3 data-v-63864230="">剧情简介</h3>
                <p data-v-63864230="">
                  %s
                </p></div>
            </div>
            <div data-v-63864230="" class="el-col el-col-24 el-col-xs-8 el-col-sm-4"><p data-v-63864230=""
                                                                                        class="score m-t-md m-b-n-sm">
              9.5</p>
            </div>
          </div>
        </div>
        <div class="el-loading-mask" style="display: none;">
          <div class="el-loading-spinner">
            <svg viewBox="25 25 50 50" class="circular">
              <circle cx="50" cy="50" r="20" fill="none" class="path"></circle>
            </svg><!----></div>
        </div>
      </div>
    </div>
  </div>
</div>
        """
        html2End = """
          <!--调用其他HTML-->
      <div style="width: 100%;overflow: hidden;">
    <div style="float:left;width: 50%;float: left;">
      <object style="border:0px" type="text/x-scriptlet" data="http://127.0.0.1:5000/CommentList" width=100% height=1600></object>
    </div>
    <div style="float:right;width: 50%;float: right;">
      <object style="border:0px" type="text/x-scriptlet" data="http://127.0.0.1:5000/visu" width=100% height=1600></object>
    </div>
</div>


</div>
</body>
        """
        # 图片后缀，名字，arr， 简介
        html2 = html2 % (data[6].split('/')[-1], data[2], data[7], data[8]) + html2End
        with open(f"templates/secondPage.html", "w", encoding="utf-8") as f:
            f.write(html2)

class GetVisu:
    def __init__(self):
        # {'2021-12'： [10, 5, 3]}
        # 日期：正向，中性，负向
        self.pieData = {}
        # 人数和评分树状图的数据
        self.xyData = {'10': 0, '20': 0, '30': 0, '40': 0, '50': 0}
        # 把图标整合到一个页面
        self.page = Page(layout=Page.SimplePageLayout)

    # 统计饼图数据
    def pieDataCount(self, commentData):
        '''
        commentData =
        [{'评星': '40', '日期': '2021', '简介': '索尼还犹豫什么啊！《超凡3》搞起啦！！！！'},
        {'评星': '50', '日期': '2021-12-15 18:52:53', '简介': '这一次，他抓住了她!'},
         '''
        for i in commentData:
            time = datetime.datetime.strptime(i['日期'], '%Y-%m-%d %H:%M:%S').strftime("%Y")
            mark = int(i['评星'])
            if time in self.pieData:
                if mark == 30:
                    self.pieData[f'{time}'][1] += 1
                elif mark < 30:
                    self.pieData[f'{time}'][2] += 1
                else:
                    self.pieData[f'{time}'][0] += 1
            else:
                if mark == 30:
                    self.pieData[f'{time}'] = [0, 1, 0]     # 好评，中评，差评
                elif mark < 30:
                    self.pieData[f'{time}'] = [0, 0, 1]
                else:
                    self.pieData[f'{time}'] = [1, 0, 0]

    # 生成饼图
    def svaePie(self):
        # 按建对字典排序（日期排序）
        newPieData = {}
        for i in sorted(self.pieData):
            newPieData.update({i: self.pieData[i]})

        tl = Timeline(init_opts=opts.InitOpts(width="500px"), )
        for i, j in newPieData.items():
            pie = (
                Pie()
                    .add(
                    "时间：{}".format(i),
                    # 要遵循这种格式[['衬衫', 33], ['毛衣', 140], ['领带', 117]]
                    [['好评', j[0]], ['中评', j[1]], ['差评', j[2]]],
                    rosetype="radius",
                    radius=["30%", "55%"],
                )
                    .set_global_opts(title_opts=opts.TitleOpts('评分与年份分析图'))
            )
            tl.add(pie, "{}年".format(i))
        # tl.render("时间饼图.html")
        self.page.add(tl)

    # 生成人数和评分树状图
    def saveXY(self, commentData):

        for i in commentData:
            self.xyData[f"{i['评星']}"] += 1
        c = (
            Bar()
                .add_xaxis(list(self.xyData))
                .add_yaxis("各评分人数", list(self.xyData.values()), color='#2f4554')
                .set_global_opts(title_opts=opts.TitleOpts(title="电影评分占比"),
                                 yaxis_opts=opts.AxisOpts(name="人数"),
                                 xaxis_opts=opts.AxisOpts(name="评分")
                                 )
        )
        # .render("各评分人数柱状图.html")
        self.page.add(c)

    # 生成词云
    def saveWordCloud(self, wordPL):
        # 字典转元组列表
        wordPL = collections.Counter(wordPL)
        # 选取频率最高的50个
        wordPLTop = wordPL.most_common(50)
        # 引用pyecharts库生成词云
        a = (
            WordCloud(init_opts=opts.InitOpts(width='800px'))
                .add(series_name="词频", data_pair=wordPLTop, word_size_range=[12, 100])
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="电影分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
                ),

                tooltip_opts=opts.TooltipOpts(is_show=True),
            )
            # .render("电影评论词云.html")
        )
        self.page.add(a)

    def main(self, commentData, wordPL):
        self.pieDataCount(commentData)
        self.saveXY(commentData)
        self.saveWordCloud(wordPL)
        self.svaePie()
        self.page.render("templates/visu.html")

class CommentList:
    def __init__(self):
        pass
    def saveCommentListHTML(self, htmlLis):
        htmlHead = """
        <head>
    <meta charset="UTF-8">
    <title>text</title>
    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport'/>
    <meta name="viewport" content="width=device-width"/>
    <link rel="stylesheet" href="{{ url_for('static', filename='/css/pinglun.css') }}">
    <style>
        .test{
            height: auto;
            margin: 0 15%;
        }
    </style>
</head>
        """
        htmlBody = """
        <body>
<div class="test">
    <div lang="en-US" class="gitment-container gitment-comments-container">
        <ul class="gitment-comments-list">
        %s
        </ul>
    </div>
</div>
</body>
        """ % htmlLis
        html = htmlHead+htmlBody
        with open(f"templates/CommentList.html", "w", encoding="utf-8") as f:
            f.write(html)

    def oneUserComment(self, comment):
        htmlLi = """
        <li class="gitment-comment">
                <a class="gitment-comment-avatar">
                    <img class="gitment-comment-avatar-img" src="%s">
                </a>
                <div class="gitment-comment-main">
                    <div class="gitment-comment-header">
                        <a class="gitment-comment-name">
                            %s
                        </a>
                        <span>评星：%d星 %s</span>

                        <div class="gitment-comment-like-btn">
                            <svg class="gitment-heart-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50">
                                <path d="M25 39.7l-.6-.5C11.5 28.7 8 25 8 19c0-5 4-9 9-9 4.1 0 6.4 2.3 8 4.1 1.6-1.8 3.9-4.1 8-4.1 5 0 9 4 9 9 0 6-3.5 9.7-16.4 20.2l-.6.5zM17 12c-3.9 0-7 3.1-7 7 0 5.1 3.2 8.5 15 18.1 11.8-9.6 15-13 15-18.1 0-3.9-3.1-7-7-7-3.5 0-5.4 2.1-6.9 3.8L25 17.1l-1.1-1.3C22.4 14.1 20.5 12 17 12z"></path>
                            </svg>
                            %s
                        </div>
                    </div>
                    <div class="gitment-comment-body gitment-markdown"><p>%s</p></div>
                </div>
                </li>
        """
        htmlLi = htmlLi % (comment['头像'], comment['昵称'], int(comment['评星'])/10, comment['日期'], comment['点赞数'], comment['简介'])
        return htmlLi

    '''
            commentData =
            [{'评星': '40', '日期': '2021', '简介': '索尼还犹豫什么啊！《超凡3》搞起啦！！！！'},
            {'评星': '50', '日期': '2021-12-15 18:52:53', '简介': '这一次，他抓住了她!'},
             '''
    def main(self, commentData):
        htmlLiS = """"""
        for i in commentData:
            htmlLiS += self.oneUserComment(i)

        self.saveCommentListHTML(htmlLiS)
