# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging
import re

from base_module import BasePage, News

class HnkjPage(BasePage):
    '''
    http://nyinfo.hnkjonline.net/xxgk.htm
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(HnkjPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_tr = soup.find_all(name="tr", attrs={"id":re.compile(r"line1070_(\d)+")})
        return all_tr
    
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a")['title']
        href = self._app_url.url + "/" + news_soup.find("a")["href"]
        date = news_soup.find_all('td')[3].string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    