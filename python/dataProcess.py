#!/usr/bin/python
# -*- coding: utf-8 -*-
path = "../data/test.csv"
w_path = "../data/new.csv"

with open(w_path, 'w') as w:
	with open(path,'r') as p:
		for line in p.readlines()[:10]:
			user_id = line.split(",")[0]
			age_range = line.split(",")[1]
			gender = line.split(",")[2]
			m_id = line.split(",")[3]
			seq = (user_id, age_range, gender, m_id)
			new_line = ",".join(seq)
			w.write(new_line)
			w.write("\n")


