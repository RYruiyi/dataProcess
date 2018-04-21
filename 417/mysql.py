#!usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

db=MySQLdb.connect('localhost','root','123456','pangpang')
cursor=db.cursor()
path="../data/new_s.csv"
sql="SELECT user_id,m_id FROM taobao WHERE m_id>= 1000 ORDER BY m_id" 

try:
	with open(path,"w") as f:
		cursor.execute(sql)
		db.commit()
		result=cursor.fetchall()
		for line in result:
			u=line[0]
			m=line[1]
			seq=(u,m)
			f.write(",".join(seq))
except:
	print "Error"
	db.rollback()

db.close()
