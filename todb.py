#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   File    :   todb.py
#   Author  :   itsjoe
#   E-mail  :   itsjoe@163.com
#

import sqlite3

class ToDB:
	
	def __init__(self, db_name, list_to_db):
		self.dbname = db_name
		self.goal = list_to_db
		self.conn = sqlite3.connect("%s"%self.dbname)
		self.cur = self.conn.cursor()
	def creat_table(self):
		self.cur.execute("create table lgsp (companyFullName text,businessZones text,companyLabelList text,financeStage text,firstType text,district text,companyShortName text,city text,industryField text,positionAdvantage text,jobNature text,positionName text,deliver text,companySize text,education text,positionLables text,workYear text)")

	def updatedb(self):
		for bg in self.goal:
			self.cur.execute("insert into lgsp values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",bg)
		self.conn.commit()
		self.conn.close()

