#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   File    :   lgSp.py
#   Author  :   itsjoe
#   E-mail  :   itsjoe@163.com
#

import lgSp.connet
import lgSp.analy
import lgSp.todb
import logging
import sys
logging.basicConfig(
	filename = "lgSp.log",
	format = "%(levelname)-10s %(asctime)s %(funcName)s %(message)s",
	level    = logging.INFO
	)

def getfilter():
	print("url = ")
	url = 'https://www.lagou.com/jobs/positionAjax.json'##sys.stdin.readline().encode("utf-8")
	print("gj = ")
	gj = input().encode('utf-8')
	print("city = ")
	city = input().encode("utf-8")
	data = {"gj":gj,"city":city,"pn":"1",'first':'true','kd':'python'}
	db_name = 'lite.sqlite3'
	return url,data,db_name

def ifempty(list_to_db):
	if list_to_db == '':
		logging.error("没有信息了")
		print("没有信息了")
	else:
		print("成功链接到一页！")

if __name__ == '__main__':
	##录入信息
	##链接
	##解析
	##录入sqlite数据库

	url,data,db_name = getfilter()
	conne = lgSp.connet.Connet(url, data)
	connc = conne.gettext()
	objc = lgSp.analy.Analy(connc)
	pagenum = objc.load_jc()
	for i in range(2, pagenum+1):
		list_to_db = objc.analysist_jc()
		print('正在执行第 %d 页'%(i-1))
		ifempty(list_to_db)
		T = lgSp.todb.ToDB(db_name,list_to_db)
		if i == 2 : T.creat_table()
		T.updatedb()
		logging.info('第 %d 页 ： 成功写入%s.sqlite3',i-1,db_name)
		data['pn'] = str(i)
		connc = lgSp.connet.Connet(url, data)
		connc = conne.gettext()
		objc = lgSp.analy.Analy(connc)
	logging.error("完成")
	print("完成")
