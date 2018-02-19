# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging
from urlparse import urlparse


from base_module import BasePage, News

class SxinfoPage(BasePage):
    '''
    http://www.sxinfo.gov.cn/tzgg/index.jhtml
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(SxinfoPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_tr = soup.find('div', {'align':'center'}).find('table').find_all('tr')
        return all_tr[1:]
    
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a").string
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find_all("td")[2].string
        dateTime = datetime.datetime.strptime(date, '%Y.%m.%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    
