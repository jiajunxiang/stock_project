#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/18
import time

import pymysql

now=time.strftime("%Y.%m.%d", time.localtime())

db=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123123',
    db='yao',
    # 字符串类型
    charset='utf8',
    # 自动二次确认
  	autocommit = True
)
# 使用cursor()方法获取操作游标
cursor = db.cursor()

def deleteWarehousing(id):
    sql = "delete from outbound_record_copy1 where outbound_record_id='{}'".format(id);
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
    except:
        print("Error")
        cursor.close()
        # 关闭数据库连接
        db.close()

def search(id):
    sql = f"select average_cost,cost,other from base_copy where id='{id}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

if __name__ == '__main__':
    a=search('000022')
    print(a)
    
    

