# coding=UTF-8

'''
Created on 2015年8月5日

@author: hp
'''

import datetime
import logging

from main.module.base_module import BasePage, News


class ZscqPage(BasePage):
    '''
    #天津知识产权局
    http://zscq.tj.gov.cn/xwdt/tztg/
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(ZscqPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        # print soup
        all_li = soup.find('div', {'class': 'right_list_b'}).find_all('li')
        all_news = []
        num = len(all_li)
        for i in range(0, num, 3):
            # 3个li表示1条新闻，[图标，链接，日期]
            all_news.append([all_li[i + 1], all_li[i + 2]])
        return all_news

    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup[0].find("a").string
        href = self._app_url.url + news_soup[0].find("a")["href"]
        date = news_soup[1].string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
