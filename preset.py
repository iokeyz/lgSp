#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   File    :   preset.py
#   Author  :   itsjoe
#   E-mail  :   itsjoe@163.com   
#

import json

def COOKIES():

	try:
		c = open('cookies.txt', mode = 'r')
		cookies = json.loads(c.__str__())
	except:
		print("Worning: 请将cookies.txt文件放入文件夹！！")
		print("Worning: 未找到cookies.txt将使用自带cookies！！")
		cookies = {
			'JSESSIONID': '99021FFD6F8EC6B6CD209754427DEA93',
            '_gat': '1',
            'user_trace_token': '20170203041008-9835aec2-e983-11e6-8a36-525400f775ce',
            'PRE_UTM': '',
            'PRE_HOST': '',
            'PRE_SITE': '',
            'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F',
            'LGUID': '20170203041008-9835b1c9-e983-11e6-8a36-525400f775ce',
            'SEARCH_ID': 'bfed7faa3a0244cc8dc1bb361f0e8e35',
            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486066203',
            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486066567',
            '_ga': 'GA1.2.2003702965.1486066203',
            'LGSID': '20170203041008-9835b03a-e983-11e6-8a36-525400f775ce',
            'LGRID': '20170203041612-714b1ea3-e984-11e6-8a36-525400f775ce'}
	return cookies


UA = [  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
		'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)']

headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Accept-Encoding': 'gzip, deflate',
           'Host': 'www.lagou.com',
           'Origin': 'http://www.lagou.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://www.lagou.com',
           'Proxy-Connection': 'keep-alive',
           'X-Anit-Forge-Code': '0',
           'X-Anit-Forge-Token': None}
