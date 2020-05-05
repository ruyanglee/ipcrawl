# coding=UTF-8

import time
import datetime
import logging
from urllib.parse import urlparse
from main.module.base_module import BasePage, News
from bs4 import BeautifulSoup

from main.app_main import driver

############################# 国家 #################################

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

############################# 北京 #################################

'''
北京市知识产权局	http://zscqj.beijing.gov.cn/col/col5652/index.html
新闻内容在<script language="javascript">中渲染
'''
class BjZscqjPage(BasePage):
    def parseAllNews(self, soup):
        # 使用selenium来加载动态js网页
        driver.get(self._app_url.url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', {'class': 'subpageCon-conList'}).find_all('tr', {'style': 'border-bottom:1px dashed #e7e7e7;'})
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


'''
海淀区知识产权服务平台
http://www.bjhd.gov.cn/cip/tzgg2013/  
'''
class HdZscqPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('ul', {'class': 'listLi'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a').string
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find('span', {'class': 'date'}).string.strip()
        dateTime = datetime.datetime.strptime(date, '[%Y-%m-%d]').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)



'''
中关村知识产权局
http://www.zgcip.org.cn/ggtz/index.jhtml?channelId=99
'''
class ZgcipPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find_all('div', {'class': 'contentlist_left'})
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('div', {'style': 'float:left'}).string
        href = news_soup.find("a")["href"]
        date = news_soup.find('span', {'class': 'time'}).string.strip() # 发布时间: 2020-04-21 09:52:46
        dateTime = datetime.datetime.strptime(date[5:].strip(), '%Y-%m-%d %H:%M:%S').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 河北 #################################

'''
河北省市场监督局（知识产权局）
http://scjg.hebei.gov.cn/node/344
'''
class HeBeiScjgPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'zkmmr_tl1_list'}).find_all('div', {'class':'zkmmr_tl1_item'})
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.a.div['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.a["href"]
        date = news_soup.a.find('p', {'class':'zkmmr_tl1_item_date'}).string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
石家庄市场监督局（知识产权局）
http://scjg.sjz.gov.cn/col/1490159811930/index.html
'''
class SjzScjgPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'center'}).find_all('div', {'style':'margin-left:6px;margin-right:6px;border-bottom:dashed 1px #959595;height:40px;'})
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find('div', {'style': 'float:right;line-height:40px;font-size:14px;color:#959595'}).string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
秦皇岛市场监督局（知识产权局） 
http://scj.qhd.gov.cn/list/12_%E6%96%B0%E9%97%BB%E5%8A%A8%E6%80%81_15_%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A.html
新闻内容在<script language="javascript">中渲染
'''
class QhdScjPage(BasePage):
    def parseAllNews(self, soup):
        # 使用selenium来加载动态js网页
        driver.get(self._app_url.url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', {'class': 'news-con'}).find('ul').find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find('a')['href']
        date = news_soup.find('span').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y/%m/%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 广东 #################################


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

############################# 江苏 #################################

'''
江苏省知识产权局	 
http://jsip.jiangsu.gov.cn/col/col75908/index.html?number=ZS0105
'''
class JsipPage(BasePage):
    def parseAllNews(self, soup):
        cnt = soup.find('div', {'id': 'div75904'}).string
        cnt = cnt.replace('<![CDATA[', '')
        cnt = cnt.replace(']]>', '')
        sp = BeautifulSoup(cnt, 'html.parser')
        all_news = sp.find_all('record')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('div', {'class': 'text'}).get_text().strip()
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        # date = news_soup.find('td', {'class':'fontbrown'}).string.strip()
        date = news_soup.find('div', {'class': 'text-date'}).get_text().strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
苏州市市场监督局	http://scjgj.suzhou.gov.cn/szqts/tzgg/nav_xwtz.shtml
'''
class SuzhouScjgjPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'cont mt10'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find('a')['href']
        date = news_soup.find('span').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)



############################# 海南 #################################

'''
海南省知识产权局
http://amr.hainan.gov.cn/szscqj/xxgk/tzgg/ 
'''
class HainanAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'gly-r-nr2'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        href = self._app_url.url + news_soup.find("a")['href']
        date = news_soup.find('em').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
海口市知识产权局
http://amr.haikou.gov.cn/xxgk/gsgg/   
'''
class HaikouAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'con-right'}).find_all('div', {'class': 'list_div'})
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        href = self._app_url.url + news_soup.find("a")['href']
        date = news_soup.find('span', {'class': 'reltime'}).string.strip()
        dateTime = datetime.datetime.strptime(date[5:].strip(), '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 湖南 #################################

'''
湖南省市场监督局
http://amr.hunan.gov.cn/amr/zwx/xxgkmlx/tzggx/index.html
'''
class HunanAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'gkgd-con-1'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find("span").string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)



############################# 上海 #################################

'''
上海市知识产权局
http://sipa.sh.gov.cn/tzgg/ 
'''
class ShSipaPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('ul', {'class': 'uli14 nowrapli no-margin list-date'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find("span").string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y.%m.%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 四川 #################################
'''
四川省知识产权服务促进中心
http://scipspc.sc.gov.cn/dtzwxx/ggl/
'''
class ScipspcPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'r_list'}).find_all('dd')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = self._app_url.url + news_soup.find("a")['href']
        date = news_soup.find("span").string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


'''
#成都市科学技术局(知识产权局)
http://cdst.chengdu.gov.cn/cdkxjsj/c108728/part_list_more.shtml 
'''
class CdstPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'borList'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a").string
        href = news_soup.find("a")['href']
        date = news_soup.find("span").string.strip()
        dateTime = datetime.datetime.strptime(date, '%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)





############################# 陕西 #################################
'''
#陕西省知识产权局
http://xakj.xa.gov.cn/kjdt/tzgg/1.html
'''
class SnipaPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'zwwk'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + '/' + news_soup.find("a")["href"]
        date = news_soup.a.next_sibling.string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
#西安市科技局（知识产权局）
http://xakj.xa.gov.cn/kjdt/tzgg/1.html
'''
class XakjPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'col-sm-9 col-md-9 hidden-xs'}).find_all('article')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find("div", {'class':'year'}).string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 内蒙古 #################################
'''
内蒙古市场监督局
http://amr.nmg.gov.cn/zw/tzgg/ 
'''
class NmgAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'top_right_con'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find('span', {'class':'xx hhhei16'}).string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 安徽 #################################
'''
安徽省市场监督局（知识产权局）
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


############################# 江西 #################################
'''
江西省市场监督局（知识产权局）
http://amr.jiangxi.gov.cn/col/col22493/ 
'''
class JiangxiAmrPage(BasePage):
    def parseAllNews(self, soup):
        cnt = soup.find('div', {'id': '336287'}).string
        cnt = cnt.replace('<![CDATA[', '')
        cnt = cnt.replace(']]>', '')
        sp = BeautifulSoup(cnt, 'html.parser')
        all_news = sp.find_all('record')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 湖北 #################################
'''
#湖北省知识产权局
http://zscqj.hubei.gov.cn/fbjd/tzgg/  
网页内容是JavaScript加载，要调整
'''
class HubeiZscqjPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('ul', {'class': 'list-b b4 row hover-style3'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = news_soup.find("a")["href"]
        date = news_soup.find("div", {'class':'calendar'}).string
        dateTime = datetime.datetime.strptime(date, '%Y-%m').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
#武汉市科技局（知识产权局）
http://kjj.wuhan.gov.cn/wmfw/tzgg/
'''
class WuhanKjjPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'list_news clearfix'}).find_all('ul')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a").string
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find('span').string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)



############################# 山东 #################################
'''
#山东市市场监督局（知识产权局）
http://amr.shandong.gov.cn/col/col76510/index.html?number=SD1002  
网页内容是JavaScript加载，要调整
'''
class ShandongAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('table', {'class': 'xxlb-tr'}).find('tbody').find_all('tr')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = news_soup.find("a")["href"]
        date = news_soup.find("td", {'width':'137'}).string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

'''
山东省知识产权事业发展中心
http://www.sdipo.net/col/col106094/index.html SdipoPage 
'''
class SdipoPage(BasePage):
    def parseAllNews(self, soup):
        cnt = soup.find('div', {'id': '251396'}).string
        cnt = cnt.replace('<![CDATA[', '')
        cnt = cnt.replace(']]>', '')
        sp = BeautifulSoup(cnt, 'html.parser')
        all_news = sp.find_all('record')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a').span.previous_sibling
        href = news_soup.find("a")["href"]
        date = news_soup.find("a").find('span').string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)




############################# 浙江省 #################################

'''
#浙江省市场监督局（知识产权局）
http://zjamr.zj.gov.cn/col/col1228969897 ZjAmrPage
'''
class ZjAmrPage(BasePage):
    def parseAllNews(self, soup):
        cnt = soup.find('div', {'id': '5324848'}).string
        cnt = cnt.replace('<![CDATA[', '')
        cnt = cnt.replace(']]>', '')
        sp = BeautifulSoup(cnt, 'html.parser')
        all_news = sp.find_all('record')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find('a')['title']
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find_all("td")[1].string.strip()
        dateTime = datetime.datetime.strptime(date, '[%Y-%m-%d]').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 重庆市 #################################

'''
#重庆市知识产权局
http://zscqj.cq.gov.cn/html/tzgg/ CqipoPage
'''
class CqipoPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'sortlist pagefk'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a").string
        parsed_uri = urlparse(self._app_url.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        href = domain + news_soup.find("a")["href"]
        date = news_soup.find("span").string
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)



############################# 吉林 #################################

'''
#吉林市场监督局
http://scjg.jl.gov.cn/zw/zxtz/  JilinScjgPage
'''
class JilinScjgPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('ul', {'class': 'index_news_list2'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = self._app_url.url + news_soup.find("a")["href"]
        dateTime = datetime.date.today()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, time.strftime('%Y-%m-%d')))
        return News(href, title, dateTime)




############################# 辽宁 #################################

'''
#辽宁省知识产权局
http://zscq.ln.gov.cn/gztz/ LiaoningZscqPage
'''
class LiaoningZscqPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('ul', {'class': 'gllist'}).find_all('li')
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a").string  # TODO 解析title乱码
        original_encoding = self.get_soup().original_encoding
        title = str(title).encode(original_encoding).decode("gbk")
        href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find("span").string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 深圳 #################################
'''
#深圳市市场监督局（知识产权局）
http://amr.sz.gov.cn/xxgk/zcwj/scjgfg/  ShenzhenAmrPage
'''
class ShenzhenAmrPage(BasePage):
    def parseAllNews(self, soup):
        all_news = soup.find('div', {'class': 'publicList'}).find_all('li', {'class':'pclist'})
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = news_soup.find("a")["href"]  #绝对路径
        if(href.find('http') == -1): # 相对路径
            href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find('a').find("span").string.strip()
        dateTime = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)


############################# 福建 #################################

'''
#福建省市场监督局（知识产权局）
http://zjj.fujian.gov.cn/scjggg/  FujianZjjPage
'''
class FujianZjjPage(BasePage):
    def parseAllNews(self, soup):
        all_ul = soup.find('div', {'class': 'gl_content'}).find_all('ul', {'class':'list'})
        all_news = all_ul[0].find_all('li')
        for ul in all_ul[1:]:
            for li in ul.find_all('li'):
                all_news.append(li)
        return all_news

    def parseNews(self, news_soup):
        title = news_soup.find("a")['title']
        href = news_soup.find("a")["href"]  #绝对路径
        if(href.find('http') == -1): # 相对路径
            href = self._app_url.url + news_soup.find("a")["href"]
        date = news_soup.find("span").string.strip()
        dateTime = datetime.datetime.strptime(date, '[%Y-%m-%d]').date()
        logging.debug("title: %s | href: %s | date: %s" % (title, href, date))
        return News(href, title, dateTime)

