# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging

from base_module import BasePage, News

class TjipoPage(BasePage):
    '''
    http://www.tjipo.gov.cn/xwdt/tztg/
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(TjipoPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        ret = []
        div = soup.find('div', {'class':'right_list_b'})
        all_li = div.find_all('li')
        i = 1
        while i < len(all_li):
            ret.append([all_li[i], all_li[i+1]])
            i = i + 3
        return ret
        
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup[0].find("a").string
        href = self._app_url.url + '/' + news_soup[0].find("a")["href"]
        date = news_soup[1].string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    