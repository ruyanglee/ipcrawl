# coding=UTF-8

'''
Created on 2019年11月24日

@author: li_zhuo@163.com
'''
import datetime
import logging
from urlparse import urlparse

from base_module import BasePage, News

class HunanIpoPage(BasePage):
    '''
    湖南省知识产权局
    http://ipo.hunan.gov.cn/xxgk/tzgg/
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(HunanIpoPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_news = soup.find('div', {'class': 'main_list_right'}).find('tbody').find_all('tr')
        return all_news
    
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a")['title']
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find_all("td")[2].string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
