#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   File    :   connet.py
#   Author  :   itsjoe
#   E-mail  :   itsjoe@163.com
#


import requests
import logging
import lgSp.preset
import random
logging.basicConfig(
	filename = "lgSp.log",
	format="%(levelname)-10s %(asctime)s %(funcName)s %(message)s",
	level    = logging.INFO
	)

class Connet:
	
	'''
	链接到拉勾网，获取信息
	'''

	def __init__(self, url, data):
		self.url = url
		self.data = data
		self.Headers = lgSp.preset.headers
		self.Headers['User-agent'] = lgSp.preset.UA[random.randint(1,len(lgSp.preset.UA))]
		self.Cookies = lgSp.preset.COOKIES()

	def gettext(self):
		try:
			c = requests.post(self.url, data = self.data, headers = self.Headers, cookies = self.Cookies)
			if c.text[:3] == '<!DO':
				logging.error('链接到拉勾被禁止!')
				return ''
			else:
				return c.text
		except Exception as e:
			logging.error(e.__str__())
			return ''

