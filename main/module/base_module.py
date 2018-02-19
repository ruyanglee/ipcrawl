# coding=UTF-8

'''
Created on 2015年8月4日

@author: hp
'''
import os
import sys
import urllib
import logging
from bs4 import BeautifulSoup

#cur_path = os.path.dirname(os.path.realpath(__file__))
cur_path = os.path.dirname(os.path.abspath(sys.argv[0]))

class News(object):
    '''
    新闻对象，基本元素包括标题、内容链接、时间
    '''
    
    href = None
    title = None
    time = None
    
    def __init__(self, href, title, time):
        '''
        Constructor
        '''
        self.href = href
        self.time = time
        self.title = title 
        
class BasePage(object):
    '''
    页面基类，解析新闻列表和新闻内容，比较是否包含关键词、满足时间范围等。
    对于一个新的页面，可以继承此基类。重载parseAllNews和parseNews方法。
    '''
        
    _app_url = None
    _app_conf = None
    
    def __init__(self, app_conf=None, app_url=None):
        '''
        Constructor
        @param app_conf: {@link AppConf}对象
        @param app_url: {@link AppUrl}对象  
        '''
        self._app_conf = app_conf
        self._app_url = app_url
    
    def set_app_conf(self, app_conf):
        self._app_conf = app_conf
    
    def set_app_url(self, app_url):
        self._app_url = app_url
        
    def filterNews(self):
        '''
        解析新闻列表
        @param name: 标签名
        @param attr: 属性，形如{'data-custom':'custom'}字典形式
        '''
        logging.info(u'---------- 开始抓取网页内容，并筛选新闻结果。----------')
        logging.info(u'抓取网址：%s' % self._app_url.url)
        cnt = self.requestPage(self._app_url.url)
        if cnt == None:
            return
        
        # 用beautifulsoup解析网页内容
        try:
            soup = BeautifulSoup(cnt, 'html.parser')
            logging.debug(u'网页格式：%s' % soup.original_encoding)
            all_news = self.parseAllNews(soup)
            for nw in all_news:
                news = self.parseNews(nw)
                flag = self.hitNews(news)
                if(flag):
                    # 保存页面并输出
                    self.saveNews(news, cur_path+'/../files/')
        except Exception, e:
            logging.error(u'解析网页内容出错，无法筛选新闻结果。错误原因：%s' % e)
            return

    def requestPage(self, url):
        '''
        根据url获取页面内容
        '''
        try:
            wp = urllib.urlopen(url)
            cnt = wp.read()
            return cnt
        except Exception, e:
            logging.error(u'抓取网页出错。错误原因：%s' % e)
            return None
    
    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。
        需要实现此方法。
        '''
        pass
                
    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        需要实现此方法。
        '''
        pass
    
    def hitNews(self, news):
        '''
        检查标题关键词、发布时间范围是否匹配设置
        '''
        # 检查日期范围
        if (news.time < self._app_conf.beginTime or news.time > self._app_conf.endTime):
            logging.debug(u'新闻时间不满足指定范围')
            return False
        
        # 检查关键字是否命中
        for word in self._app_conf.keywords:
            if(news.title.find(word) > -1):
                return True
        logging.debug(u'新闻标题没有命中关键字。新闻标题: ' + news.title)
        return False
    
    def saveNews(self, news, local_dir):
        '''
        匹配的新闻，保存内容到本地
        '''
        logging.info(u'找到匹配新闻。新闻标题: %s, 新闻链接: %s, 新闻时间: %s' % (news.title, news.href, news.time))
        try:
            article_content = self.requestPage(news.href)
            fp = open(local_dir + news.title + ".html", "w")  # 打开一个文本文件
            fp.write(article_content)  # 写入数据
            fp.close()  # 关闭文件
        except Exception, e:
            logging.error(u'保存该新闻出错，错误原因：%s' % e)
            