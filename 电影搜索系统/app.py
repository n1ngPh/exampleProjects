# -*- coding:utf-8 -*-
# @Time : 2022/4/19 12:40
# @File : app.py.py
# @Software : PyCharm
import getHTML
import gotoMySQL
import dbData
from flask import Flask, render_template, request


temp = 0
app = Flask(__name__)
token1 = ''


# 一级界面
@app.route("/")
def firstpage():
    return render_template('/page1.html')


@app.route("/page/<i>")
def firstpages(i):
    return render_template(f'/page{i}.html')


# 二级界面
@app.route("/token/<token>")
def goto(token):
    global token1
    token1 = token

    data = []
    rmyql = gotoMySQL.GotoMySQL(0)
    for i in rmyql.readMysql():
        if i[1] == token:
            data = i
            break
    # print(data)
    getHTML.GetHTML2().saveHTML2(data)
    return render_template('/secondPage.html')


# 二级界面的图表
@app.route("/visu")
async def goto2():
    commentData, wordPL = dbData.Visu().getCommentData(token1)
    getHTML.GetVisu().main(commentData, wordPL)
    # print(commentData)
    return render_template('/visu.html')

# 二级界面的评论
@app.route("/CommentList")
async def goto22():
    commentData, wordPL = dbData.Visu().getCommentData(token1)
    getHTML.CommentList().main(commentData)
    return render_template('/CommentList.html')


# 接受搜索框电影名称
@app.route('/name', methods=['GET', 'POST'])
def wstm_search():
    # 当接受到post请求时
    cearch_token = ''
    if request.method == 'POST':
        # 取出待搜索keyword
        movieName = request.form['keyword']
        rmyql = gotoMySQL.GotoMySQL(0)
        for i in rmyql.readMysql():
            if i[2] == movieName:
                cearch_token = i[1]
                goto(cearch_token)
                break
    if cearch_token == '':
        return render_template('/notFound.html')
    else:
        return render_template('/secondPage.html')


# debug=True实时更新，use_reloader=False 停止flask加载两次
def main():
    app.run(debug=True, host='127.0.0.1', port='5000',  use_reloader=False)


main()
