# coding=UTF-8

import datetime
import logging

from base_module import BasePage, News

class JstdPage(BasePage):
    '''
    http://www.jstd.gov.cn/zwgk/tzggg/index.html
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(JstdPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        ret = []
        news = soup.find_all('td', {'width':'581', 'height':'22', 'style':'vertical-align:middle'})
        date = soup.find_all('td', {'width':'180', 'align':'center', 'style':'vertical-align:middle;color:#999999'})
        for i in range(len(news)):
            ret.append([news[i], date[i]])
        return ret
        
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup[0].find("a")['title'].strip()
        href = news_soup[0].find("a")['href']
        date = news_soup[1].get_text().strip()
        dateTime = datetime.datetime.strptime(date, '(%Y-%m-%d)').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    