#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   File    :   analy.py
#   Author  :   itsjoe
#   E-mail  :   itsjoe@163.com
#

import lgSp.connet
import json
import logging
logging.basicConfig(
	filename = "lgSp.log",
	format = "%(levelname)-10s %(asctime)s %(funcName)s %(message)s",
	level    = logging.INFO
	)

class Analy:
	
	def __init__(self, jc):
		self.jc = json.loads(jc)

	def load_jc(self):
		try:
			pc = self.jc['content']['positionResult']['totalCount'] // self.jc['content']['positionResult']['resultSize'] +1
			return pc
		except Exception as e:
			logging.error(e)
			return 0

	def analysist_jc(self):
		jcll = []
		for i in range(0, self.jc['content']['positionResult']['resultSize']):
			self.jcd = self.jc['content']['positionResult']['result'][i]
			jcl = []
			jcl = [	self.jcd['companyFullName'].__str__().encode('utf-8') ,
					self.jcd['businessZones'].__str__().encode('utf-8') ,
					self.jcd['companyLabelList'].__str__().encode('utf-8') ,
					self.jcd['financeStage'].__str__().encode('utf-8') ,
					self.jcd['firstType'].__str__().encode('utf-8') ,
					self.jcd['district'].__str__().encode('utf-8') ,
					self.jcd['companyShortName'].__str__().encode('utf-8') ,
					self.jcd['city'].__str__().encode('utf-8') ,
					self.jcd['industryField'].__str__().encode('utf-8') ,
					self.jcd['positionAdvantage'].__str__().encode('utf-8') ,
					self.jcd['jobNature'].__str__().encode('utf-8') ,
					self.jcd['positionName'].__str__().encode('utf-8') ,
					self.jcd['deliver'].__str__().encode('utf-8') ,
					self.jcd['companySize'].__str__().encode('utf-8') ,
					self.jcd['education'].__str__().encode('utf-8') ,
					self.jcd['positionLables'].__str__().encode('utf-8') ,
					self.jcd['workYear']
				]
			jcll.append(tuple(jcl))
		return jcll

