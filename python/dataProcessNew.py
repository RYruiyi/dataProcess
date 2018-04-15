#!/usr/bin/python
# -*- coding: utf-8 -*-

path = "../data/test.csv"
w_path = "../data/new_all.csv"

with open(w_path, 'w') as w:
	with open(path,'r') as p:
		for line in p.readlines()[1:100]:
			split_line = line.split(",")
			user_id = split_line[0]
			age_range = split_line[1]
			gender = split_line[2]
			m_id = split_line[3]
			seq = (user_id, age_range, gender, m_id)
			new_line = ",".join(seq)
			w.write(new_line)
			w.write("\n")
