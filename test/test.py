# coding=UTF-8

import sys
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import urllib
import urllib2
import re

reload(sys)
sys.setdefaultencoding('utf8')  # @UndefinedVariable

if __name__ == "__main__":
    print("start ... ")

    url='http://amr.jiangxi.gov.cn/col/col22493/'
    session = HTMLSession()

    pg = session.get(url)
    pg.html.render(sleep=5)

    soup = BeautifulSoup(pg.html.html, "lxml")
    all_news = soup.find('div', {'class': 'common-list-items'}).find_all('li')
    print(len(all_news))

    '''
    url = "http://218.8.25.229:8003/xwzs!queryXwxxqx.action?lbbn=4"
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept':'text/html;q=0.9,*/*;q=0.8',
                    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding':'gzip',
                    'Connection':'close',
                    'Host':'218.8.25.229:8003'
                    }
    req_timeout = 5
    req = urllib2.Request(url,None,req_header)
    resp = urllib2.urlopen(req,None,req_timeout)
    html = resp.read()
    print(html)
    '''
    
    url = "http://www.jstd.gov.cn/zwgk/tzggg/index.html"
    req = urllib2.Request(url)
    cnt = urllib2.urlopen(req).read()
    soup = BeautifulSoup(cnt, 'html.parser')
    a = soup.find_all('td', {'width':'581', 'height':'22', 'style':'vertical-align:middle'})
    b = soup.find_all('td', {'width':'180', 'align':'center', 'style':'vertical-align:middle;color:#999999'})
    print len(a)
    print len(b)
    
    
    '''
    cnt = None
    url = 'http://www.hnipo.gov.cn/hnzscqj/zwgk/tz/content_29912.html'
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept':'text/html;q=0.9,*/*;q=0.8',
                    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding':'gzip',
                    'Connection':'close'
                }
    req_timeout = 10
    for i in range(10):
        print url
        #wp = urllib2.urlopen('http://www.hnipo.gov.cn/hnzscqj/zwgk/tz/content_29912.html')
        req = urllib2.Request(url, None, req_header)
        resp = urllib2.urlopen(req, None, req_timeout)
        cnt = resp.read()
        
    soup = BeautifulSoup(cnt, 'html.parser')
    all_tr = soup.find_all(name="tr", attrs={"id":re.compile(r"line1070_(\d)+")})
    print(len(all_tr))
    for tr in all_tr:
        # print(tr)
        nw = tr.find_all('td')[3]
        print(nw.string.strip())
    fp = open("pytest.html", "w")
    fp.write(cnt)
    fp.close()
    '''
    