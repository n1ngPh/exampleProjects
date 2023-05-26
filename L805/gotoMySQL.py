# -*- coding:utf-8 -*-
# @Time : 2022/4/20 17:22
# @File : gotoMySQL.py
# @Software : PyCharm


import pymysql

"""
关于数据库表的创建、写入、读取
"""

class GotoMySQL():
    def __init__(self, mark):
        # 连接到mysql数据库
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mysql', charset='utf8')
        self.cursor = self.conn.cursor()
        # 1代表考虑创建或清空表
        if mark == 1:
            try:
                # 创建表
                sql = """create table mydoubandata(
                                            m_id int primary key auto_increment,
                                            m_token varchar (10) not null,
                                            m_title varchar(30) not null,
                                            m_pingfen varchar(10) not null,
                                            m_comment text null,
                                            m_link varchar(100) not null,
                                            m_img text not null,
                                            m_arr text null,
                                            m_synopsis text null
                                            )"""
                self.cursor.execute(sql)
            except:
                # 如果表存在 就清空数据
                sql = "TRUNCATE TABLE mydoubandata"
                self.cursor.execute(sql)

    def writeMysql(self, token, title, pingfen, comment, link, img, arr, synopsis):
        # 建立存放电影数据的表mydoubanfilm,名字自取
        self.sql = 'insert into mydoubandata(m_token,m_title, m_pingfen,m_comment, m_link, m_img, m_arr, m_synopsis) values ("%s","%s","%s","%s","%s","%s","%s","%s")' % (
        token, title, pingfen, comment, link, img, arr, synopsis)
        self.cursor.execute(self.sql)

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


    def readMysql(self):
        # 需要查询的MySQL语句
        sql = "select * from mydoubandata"
        # 4.执行sql语句
        self.cursor.execute(sql)
        # 因为调用不会自动叠加，不能用fetchone
        mysqlAllData = self.cursor.fetchall()
        return mysqlAllData
