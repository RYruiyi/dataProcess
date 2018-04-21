#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

conn=MySQLdb.connect('localhost','root','123456','pangpang')
x = conn.cursor()
path = "../data/new.csv"
sql = "INSERT INTO taobao VALUES (%s,%s,%s,%s)"

try:
	with open(path, 'r') as p:
		batch_list = []
		for line in p.readlines()[1:101]:
			split_line = line.split(",")
			user_id = split_line[0]
			age_range = split_line[1]
			gender = split_line[2]
			m_id = split_line[3]
			seq = (user_id, age_range, gender, m_id)
			batch_list.append(seq)
		# 批量batch插入
   		x.executemany(sql, batch_list)
   		conn.commit()
except:
	print "something wrong.."
   	conn.rollback()

conn.close()