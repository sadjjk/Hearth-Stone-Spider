# -*- coding: utf-8 -*-
# @Author: kjjdas
# @Date:   2018-08-05 10:49:35
# @Last Modified time: 2018-08-05 19:08:34


from selenium import webdriver
from pyquery import PyQuery as pq
import requests
import time 
import re 


def get_html():
    browser=  webdriver.Chrome()
    browser.get('http://cha.17173.com/hs/')

    for i in range(90):
        browser.execute_script('var q=document.documentElement.scrollTop='+str(i*1000))
        time.sleep(1)


    time.sleep(3)
    html = browser.page_source.encode('GBK', 'ignore').decode('GBk')
    browser.close()
    return html 

def get_imgs(html):    
    img_urls = re.findall(r'return false;" target=""><img src="(.*?)"', html)
    for img_url in img_urls:
        img_url = img_url.split('?')[0]
        img_content = requests.get(img_url).content
        with open('./卡牌/'+img_url.split('/')[-1],'wb') as f:
            f.write(img_content)


def main():
    html = get_html()
    get_imgs(html)

if __name__ == '__main__':
    main()