# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging
from urlparse import urlparse

from main.module.base_module import BasePage, News
from bs4 import BeautifulSoup


class JsipPage(BasePage):
    '''
    #江苏省知识产权局
    http://jsip.jiangsu.gov.cn/col/col3256/index.html
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(JsipPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        该网页内容是js代码生成，所以特殊处理。
        '''
        cnt = soup.find('div', {'id': '6691'}).string
        cnt = cnt.replace('<![CDATA[', '')
        cnt = cnt.replace(']]>', '')
        sp = BeautifulSoup(cnt, 'html.parser')
        all_news = sp.find_all('record')
        return all_news

    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find('div', {'class': 'text'}).get_text().strip()
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        # date = news_soup.find('td', {'class':'fontbrown'}).string.strip()
        date = news_soup.find('div', {'class': 'text-date'}).get_text().strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
