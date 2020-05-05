# coding=UTF-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

import os
import sys
import datetime
from urllib.parse import urlparse

cur_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(cur_path)

chrome_options = Options()
chrome_options.add_argument('--headless')

chromedriverpath = cur_path + '/../chromedriver/win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriverpath, options=chrome_options)

# 打开目标网页
url = "http://zscqj.beijing.gov.cn/col/col5652/index.html"
driver.get(url)

# 获取网页标题
title = driver.title

# 获取html
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

all_news = soup.find('ul', {'class': 'subpageCon-conList'}).find_all('tr', {'style': 'border-bottom:1px dashed #e7e7e7;'})
print(len(all_news))

for news_soup in all_news:
    print(news_soup)
    title = news_soup.find('a')['title']
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    href = domain + news_soup.find("a")["href"]
    date = news_soup.find('font', {'color': '#808080'}).string.strip()
    dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    print("title: %s | href: %s | date: %s" % (title, href, date))

# print(soup.prettify())

# 其他api请自行百度
# ...


driver.close()
