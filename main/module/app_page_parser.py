# coding=UTF-8

import datetime
import logging
from urlparse import urlparse
from base_module import BasePage, News

'''
国家知识产权局
http://www.sipo.gov.cn/tz/gz/
'''
class SipoPage(BasePage):
    def parseAllNews(self, soup):
        '''
        解析页面，得到所有新闻元素。对于新页面，可以重载此方法。
        '''
        all_li = soup.find('div', {'class': 'index_articl_list'}).find_all('li')
        return all_li

    def parseNews(self, news_soup):
        '''
        解析标题，链接，发布日期等元素，返回News对象。
        对于新页面，可以重载此方法。
        '''
        title = news_soup.find("a").string
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
湖南省市场监督局
http://amr.hunan.gov.cn/amr/zwx/xxgkmlx/tzggx/index.html
'''
class HunanAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'listPage-r-li-xxgk'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
湖南省知识产权局
http://ipo.hunan.gov.cn/xxgk/tzgg/
'''
class HunanIpoPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'main_list_right'}).find('tbody').find_all('tr')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find_all("td")[2].string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
徽省市场监督局（知识产权局）
http://amr.ah.gov.cn/xwdt/gsgg/
'''
class AnHuiAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'navjz clearfix'}).find('ul').find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
合肥市市场监督局（知识产权局）
http://amr.hefei.gov.cn/zwgk/gggs/index.html
'''
#TODO 网站有反爬虫，未生效
class HeFeiAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'navjz clearfix'}).find('ul').find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
河北省市场监督局（知识产权局）
http://scjg.hebei.gov.cn/node/344
'''
class HeBeiScjgPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'id': 'add_rlist_content'}).find_all('div', {'class':'article_list flex flex-align-center flex-pack-justify'})
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('div', {'class':'article_list_text'}).string
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find('div', {'class':'article_list_time'}).string
        dateTime = datetime.datetime.strptime(date, '[%m-%d]').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
秦皇岛市场监督局（知识产权局） 
http://scj.qhd.gov.cn/list/12_%E6%96%B0%E9%97%BB%E5%8A%A8%E6%80%81_15_%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A.html
'''
#TODO Ajax动态加载的页面，所以抓取不到
class QhdScjPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'news-con'}).find('ul').find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find('a')['href']
        date = news_soup.find('span').string
        dateTime = datetime.datetime.strptime(date, '%Y/%m/%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
广东省市场监督局（知识产权局）
http://amr.gd.gov.cn/zwdt/tzgg/index.html   
'''
class GdAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('ul', {'class': 'news_list2 marB20'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a').string
        href = news_soup.find('a')['href']
        date = news_soup.find('span').string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
广州市市场监督局
http://gzamr.gzaic.gov.cn/gzscjgj/zwdt_tzgg/common_list.shtml 
'''
class GzscjgjPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'news_list'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        url = self._app_url.url
        href = url[0 : url.rfind('/')] + '/' + news_soup.find("a")['href']
        date = news_soup.find('span').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
佛山市市场监督局 http://fsamr.foshan.gov.cn/zwdt/tzgg/index.html
'''
class FsAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'news_list'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        url = self._app_url.url
        href = url[0 : url.rfind('/')] + '/' + news_soup.find("a")['href']
        date = news_soup.find('span').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
北京市知识产权局	http://zscqj.beijing.gov.cn/col/col5652/index.html
'''
#TODO 新闻内容在<script language="javascript">中渲染。暂时抓不到。
class BjZscqjPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('ul', {'class': 'subpageCon-conList'}).find_all('tr', {'style':'border-bottom:1px dashed #e7e7e7;'})
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find('font', {'color':'#808080'}).string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)
