#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/2/21/021 15:43
import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123123',
    db='GMS',
    # 字符串类型
    charset='utf8',
    # 自动二次确认
    autocommit=True
)
# 使用cursor()方法获取操作游标
cursor = db.cursor()

def login(name,password):
    sql = "SELECT COUNT(*) FROM user where username='{0}' and password='{1}' LIMIT 1".format(name,password);
    cursor.execute(sql)
    result=cursor.fetchone()[0]
    return result
# ====================   一、进货管理模块  ===========================
def addWarehousing(date,name,category,number):
    sql = 'insert into warehousing_record' \
          '(create_time,goods_name,goods_category,receipt_quantity) values (%s,%s,%s,%s)'
    # 插入数据
    data = [(date, name, category, number)]
    try:
        # 拼接并执行SQL语句
        cursor.executemany(sql, data)
        return cursor.rowcount
    except:
        print("Error: unable to fetch data")
def listWarehousing():
    sql = "select * from warehousing_record"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
def queryWarehousing(id):
    sql = f"select * from warehousing_record where warehousing_record_id='{id}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
def searchWarehousing(date):
    sql = f"select * from warehousing_record where create_time='{date}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
def updateWarehousing(id,date,name,category,number):
    sql = "update warehousing_record set " \
          "create_time='{0}',goods_name='{1}',goods_category='{2}',receipt_quantity='{3}' where " \
          "warehousing_record_id='{4}'".format(date,name,category,number,id)
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
        return cursor.rowcount
    except:
        print("Error: unable to modity data")
        # cursor.close()
        # # 关闭数据库连接
        # db.close()
def deleteWarehousing(id):
    sql = "delete from warehousing_record where warehousing_record_id='{}'".format(id);
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
    except:
        print("Error")
# ====================   二、出货管理模块  ===========================
def delOutbound(date,name,category,number):
    sql = 'insert into outbound_record' \
          '(create_time,goods_name,goods_category,outbound_quantity) values (%s,%s,%s,%s)'
    # 插入数据
    data = [(date, name, category, number)]
    try:
        # 拼接并执行SQL语句
        cursor.executemany(sql, data)
        return cursor.rowcount
    except:
        print("Error: unable to fetch data")
def listOutbound():
    sql = "select * from outbound_record"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
def searchOutbound(date):
    sql = f"select * from outbound_record where create_time='{date}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
def queryOutbound(id):
    sql = f"select * from outbound_record where outbound_record_id='{id}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
def updateOutbound(id,date,name,category,number):
    sql = "update outbound_record set " \
          "create_time='{0}',goods_name='{1}',goods_category='{2}',outbound_quantity='{3}' where " \
          "outbound_record_id='{4}'".format(date,name,category,number,id)
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
        return cursor.rowcount
    except:
        print("Error: unable to modity data")
        # cursor.close()
        # # 关闭数据库连接
        # db.close()
def deleteOutbound(id):
    sql = "delete from outbound_record where outbound_record_id='{}'".format(id);
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
    except:
        print("Error")

# ====================   三、库存管理模块  ===========================
def addStock(name,number):
    sql = 'insert into stock' \
          '(name,number) values (%s,%s)'
    # 插入数据
    data = [(name,number)]
    try:
        # 拼接并执行SQL语句
        cursor.executemany(sql, data)
        return cursor.rowcount
    except:
        print("Error: unable to fetch data")
def listStock():
    sql = "select * from stock"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
def searchStock(name):
    sql = f"select * from stock where name='{name}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
def queryStock(name):
    sql = f"select * from stock where name='{name}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
def updateStock(name,number):
    sql = "update stock set number='{0}' where name='{1}'".format(number,name)
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
        return cursor.rowcount
    except:
        print("Error: unable to modity data")
        # cursor.close()
        # # 关闭数据库连接
        # db.close()
def deleteStock(name):
    sql = "delete from stock where name='{}'".format(name);
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
    except:
        print("Error")
     # cursor.close()
            # # 关闭数据库连接
            # db.close()

# ====================   药品管理模块  ===========================
def add(name,number):
    sql = 'insert into base_copy' \
          '(name,number) values (%s,%s)'
    # 插入数据
    data = [(name,number)]
    try:
        # 拼接并执行SQL语句
        cursor.executemany(sql, data)
        return cursor.rowcount
    except:
        print("Error: unable to fetch data")
def list():
    sql = "select * from base_copy"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
def search(id):
    sql = f"select id,name,average_cost,cost,other from base_copy where id='{id}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def update(name,average_cost,cost,other):
    sql = "update base_copy set average_cost='{1}',cost='{2}',other='{3}' where name='{0}'".format(name,average_cost,cost,other)
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
        return cursor.rowcount
    except:
        print("Error: unable to modity data")

def delete(id):
    sql = "delete from base_copy where id='{}'".format(id);
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
    except:
        print("Error")