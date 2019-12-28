# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging

from main.module.base_module import BasePage, News

class BhgovPage(BasePage):
    '''
    http://www.bh.gov.cn/html/KWN/GGL21842/List/list_0.htm
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(BhgovPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        ret = []
        all_cnt = soup.find_all('td', {'width':'84%', 'height':'34', 'align':'left', 'valign':'middle'})
        #print all_cnt
        all_dt = soup.find_all('td', {'width':'16%', 'align':'left', 'valign':'middle', 'class':'STYLE2'})
        #print all_dt
        i = 0
        while i < len(all_cnt):
            ret.append([all_cnt[i], all_dt[i]])
            i = i + 1
        return ret
        
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup[0].find("a").string.strip().split()[-1]
        url = self._app_url.url[0:self._app_url.url.rfind('/')]
        href = url + '/' + news_soup[0].find("a")["href"]
        date = news_soup[1].string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug(u'title: %s | href: %s | date: %s' % (title, href, date))
        return News(href, title, dateTime)
    