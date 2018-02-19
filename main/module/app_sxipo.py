# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging

from base_module import BasePage, News

class SxipoPage(BasePage):
    '''
    http://www.sxipo.gov.cn:8000/zscqj/ggl/index.htm
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(SxipoPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_li = soup.find_all('div', {'class':'c1-bline'})
        return all_li
    
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a")['title']
        href = news_soup.find("a")['href']
        date = news_soup.find("div", {'class':'f-right'}).string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    
