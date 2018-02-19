# coding=UTF-8

import datetime
import logging

from base_module import BasePage, News

class SzipPage(BasePage):
    '''
    http://www.szip.gov.cn/list.aspx?id=63
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(SzipPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_li = soup.find_all("div", {"style":"background:url(images/bottom_line.jpg) bottom repeat-x; height:40px;  width:640px;"})
        return all_li
        
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a").string
        url = self._app_url.url[0:self._app_url.url.rfind('/')]
        href = url + '/' + news_soup.find("a")["href"]
        date = news_soup.find('div', {'style':'float:left; margin-top:10px; color:#b3b3b3; font-size:12px;'}).get_text().strip()
        dateTime = datetime.datetime.strptime(date, '[%Y-%m-%d]').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    