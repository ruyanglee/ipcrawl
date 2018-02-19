# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging

from base_module import BasePage, News

class CsipoPage(BasePage):
    '''
    http://csipo.changsha.gov.cn/zxzx/tzgg/
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(CsipoPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_dd = soup.find('div', {'id':'hnews2'}).find_all('dd')
        return all_dd
    
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a").string
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    