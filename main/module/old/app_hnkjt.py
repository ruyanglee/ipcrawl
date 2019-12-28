# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging

from main.module.base_module import BasePage, News

class HnkjtPage(BasePage):
    '''
    http://www.hnkjt.gov.cn/tzgg/
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(HnkjtPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_li = soup.find('div', {'class':'list_u1'}).find('ul').find_all('li')
        return all_li
        
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a").string
        href = news_soup.find("a")["href"]
        date = news_soup.find('span').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y.%m.%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    