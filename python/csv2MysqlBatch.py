#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

conn=MySQLdb.connect('localhost','root','123456','pangpang')
x = conn.cursor()
path = "../data/new_all.csv"
sql = "INSERT INTO taobao VALUES (%s,%s,%s,%s)"

try:
	with open(path, 'r') as p:
		batch_list = []
		for line in p.readlines():
			split_line = line.split(",")
			user_id = line.split(",")[0]
			age_range = line.split(",")[1]
			gender = line.split(",")[2]
			m_id = line.split(",")[3]
			seq = (user_id, age_range, gender, m_id)
			batch_list.append(seq)
		# 批量batch插入
   		x.executemany(sql, batch_list)
   		conn.commit()
except:
	print "something wrong.."
   	conn.rollback()

conn.close()