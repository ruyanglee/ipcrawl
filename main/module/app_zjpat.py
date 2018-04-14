# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging
import re
from urlparse import urlparse

from base_module import BasePage, News


class ZjpatPage(BasePage):
    '''
    #浙江省知识产权局
    http://www.zjpat.gov.cn/interIndex.do?method=list22&dir=/zjszscqj/tzgg
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(ZjpatPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_news = soup.find('table', {'class': 'mgt03'}).find_all('tr')
        return all_news

    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find('a')['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]

        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", news_soup.find_all('td')[1].string)
        date = mat.group(0).strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
