#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

conn=MySQLdb.connect('localhost','root','123456','pangpang')
x = conn.cursor()
path = "../data/new_all.csv"
sql = "INSERT INTO taobao VALUES (%s,%s,%s,%s)"


try:
	with open(path, 'r') as p:
		for line in p.readlines():
			split_line = line.split(",")
			user_id = line.split(",")[0]
			age_range = line.split(",")[1]
			gender = line.split(",")[2]
			m_id = line.split(",")[3]
			# 非批量插入
   			x.execute(sql, (user_id, int(age_range), int(gender), m_id))
   			conn.commit()
except:
	print "something wrong.."
   	conn.rollback()

conn.close()