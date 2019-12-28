# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging

from main.module.base_module import BasePage, News

class TyipoPage(BasePage):
    '''
    http://www.tyipo.gov.cn/broad.asp
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(TyipoPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_tr = soup.find('div', {'align':'center'}).find('table').find_all('tr')
        return all_tr
    
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a").string
        href = self._app_url.url + "/" + news_soup.find("a")["href"]
        #print news_soup.find_all("td")[1].find("p")
        date = news_soup.find_all("td")[1].find("p").getText().split('[')[-1].split()[0]
        #print date
        dateTime = datetime.datetime.strptime(date, '%Y/%m/%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    