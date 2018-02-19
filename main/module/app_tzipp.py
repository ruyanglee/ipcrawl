# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging
from urlparse import urlparse

from base_module import BasePage, News

class TzippPage(BasePage):
    '''
    http://www.tzipp.cn/tzzlj/zh_cn/tzgg/index.html
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(TzippPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_li = soup.find('ul', {'class':'article-items'}).find_all('li')
        return all_li
    
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a")['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '[%Y.%m.%d]').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    
