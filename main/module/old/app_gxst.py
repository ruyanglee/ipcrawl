# coding=UTF-8

import datetime
import logging
from urlparse import urlparse

from main.module.base_module import BasePage, News

class GxstPage(BasePage):
    '''
    http://www.gxst.gov.cn/zwgk/tzgg/sbtz/index.shtml
    '''

    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        '''
        super(GxstPage, self).__init__(app_conf, app_url)

    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_li = soup.find('ul', {'class':'newslist newslist2'}).find_all('li')
        return all_li
        
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a")['title'].strip()
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find('span').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y/%m/%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
    
    def saveNews(self, news, local_dir):
        '''
        匹配的新闻，保存内容到本地
        '''
        logging.info("找到匹配新闻。新闻标题: %s, 新闻链接: %s, 新闻时间: %s" % (news.title, news.href, news.time))        
        try:
            article_content = self.requestPage(news.href)
            fp = open(local_dir + news.title.split('<br>')[0] + ".html", "w")  # 打开一个文本文件
            fp.write(article_content)  # 写入数据
            fp.close()  # 关闭文件
        except Exception, e:
            logging.error("保存该新闻出错，错误原因：%s" % e)
            