# coding=UTF-8

import datetime
import logging

from base_module import BasePage, News

class NjipPage(BasePage):
    '''
    http://www.njip.gov.cn/ggtz/
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(NjipPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_li = soup.find('ul', {'class':'main_R_mid_ul'}).find_all('li')
        return all_li
        
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a")['title']
        href = self._app_url.url + '/' + news_soup.find("a")['href']
        for date in news_soup.stripped_strings:
            pass
        #print date
        dateTime = datetime.datetime.strptime(date, '[%Y年%m月%d]').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    