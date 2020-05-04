# coding=UTF-8

'''
Created on 2015年8月4日

@author: hp
'''
import os
import sys
from urllib import request
import traceback
import logging
from bs4 import BeautifulSoup

from main.app_main import ua

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
    _soup = None
    
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

    def get_soup(self):
        return self._soup

    def filterNews(self):
        '''
        解析新闻列表
        @param name: 标签名
        @param attr: 属性，形如{'data-custom':'custom'}字典形式
        '''
        logging.info('---------- 开始抓取网页内容，并筛选新闻结果。----------')
        logging.info('抓取网址：%s' % self._app_url.url)
        cnt = self.requestPage(self._app_url.url)
        if cnt == None:
            return
        
        # 用beautifulsoup解析网页内容
        all_news = None
        try:
            soup = BeautifulSoup(cnt, 'html.parser')
            self._soup = soup
            logging.info('网页格式：%s' % soup.original_encoding)
            all_news = self.parseAllNews(soup)
        except Exception as e:
            logging.error('解析网页内容出错，无法筛选新闻结果。错误原因：%s' % e)
            return

        for nw in all_news:
            news = None
            try:
                news = self.parseNews(nw)
            except Exception as e:
                logging.error('解析新闻内容出错。错误原因：%s' % e)
                continue
            flag = self.hitNews(news)
            if(flag):
                # 保存页面并输出
                self.saveNews(news, cur_path+'/../files/')

    def requestPage_urllib(self, url):
        '''
        使用urllib2来爬取页面内容
        '''
        try:
            wp = request.urlopen(url, timeout=15)
            cnt = wp.read()
            return cnt
        except Exception as e:
            logging.error('抓取网页出错：%s，错误原因：%s' % (url, e))
            return None

    # def getContent(url, headers):
    #     """
    #     此函数用于抓取返回403禁止访问的网页
    #     """
    #     random_header = random.choice(headers)
    #
    #     """
    #     对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    #     也可以直接将个字典传入，字典中就是下面元组的键值对应
    #     """
    #     req = urllib2.Request(url)
    #     req.add_header("User-Agent", random_header)
    #     req.add_header("GET", url)
    #     req.add_header("Host", "blog.csdn.net")
    #     req.add_header("Referer", "http://www.csdn.net/")
    #
    #     content = urllib2.urlopen(req).read()
    #     return content

    def requestPage(self, url):
        '''
        使用requests来爬取页面内容
        '''
        headers = {'User-Agent': ua.random}
        try:
            req = request.Request(url, None, headers)
            resp = request.urlopen(req, None, timeout=15)
            cnt = resp.read()
            return cnt
        except Exception as e:
            logging.error('抓取网页出错：%s，错误原因：%s' % (url, e))
            return self.requestPage_urllib(url) #requests方式抓取失败，再尝试用urllib2抓取
    
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
        logging.info('判断新闻是否匹配。新闻标题: %s, 新闻链接: %s, 新闻时间: %s' % (news.title, news.href, news.time))
        try:
            # 检查日期范围
            if (news.time < self._app_conf.beginTime or news.time > self._app_conf.endTime):
                logging.debug('新闻时间不满足指定范围')
                return False

            # 检查关键字是否命中
            for word in self._app_conf.keywords:
                if(news.title.find(word) > -1):
                    return True
            logging.debug('新闻标题没有命中关键字。新闻标题: ' + news.title)
            return False
        except Exception as e:
            logging.error('判断新闻是否匹配出错，错误原因：%s' % e)
            return False
    
    def saveNews(self, news, local_dir):
        '''
        匹配的新闻，保存内容到本地
        '''
        logging.info('找到匹配新闻。新闻标题: %s, 新闻链接: %s, 新闻时间: %s' % (news.title, news.href, news.time))
        try:
            # 把标题、url写入文件
            fp = open(local_dir + '00_result.txt', 'a+')  # 打开一个文本文件
            txt = '%s, %s, %s \r\n' % (news.title, news.href, news.time)
            fp.write(txt)  # 写入数据
            fp.close()  # 关闭文件

            # 把网页内容保存到本地
            article_content = self.requestPage(news.href)
            fp = open(local_dir + news.title + ".html", "wb")  # 打开一个文本文件
            fp.write(article_content)  # 写入数据
            fp.close()  # 关闭文件
        except Exception as e:
            logging.exception('保存该新闻出错，错误原因：%s' % e)
