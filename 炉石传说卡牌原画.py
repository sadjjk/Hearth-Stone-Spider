# # -*- coding: utf-8 -*-
# # @Author: kjjdas
# # @Date:   2018-08-05 00:34:43
# # @Last Modified time: 2018-08-05 18:49:31


import requests
from pyquery import PyQuery as  pq 
html = requests.get('http://news.4399.com/gonglue/lscs/kptj/').content.decode('gbk')
doc = pq(html)
items = doc('#dq_list > li').items()
# print(items)
for item in items:
    # print(item)
    url = item.find('img').attr('lz_src')
    url_content = requests.get(url).content
    name = item.find('.kp-name').text()
    with open('./卡牌原画/'+name+'.jpg','wb') as f:
        f.write(url_content)
    