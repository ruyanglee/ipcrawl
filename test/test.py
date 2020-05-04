# coding=UTF-8

import sys
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import re
import traceback
import importlib
import requests
from urllib import parse
from urllib import request
from fake_useragent import UserAgent

importlib.reload(sys)

if __name__ == "__main__":
    print("start ... ")

    ua = UserAgent()

    print(ua.ie)
    print(ua.opera)
    print(ua.chrome)
    print(ua.firefox)
    print(ua.safari)

    url='http://scj.qhd.gov.cn/list/12_%E6%96%B0%E9%97%BB%E5%8A%A8%E6%80%81_15_%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A.html'

    try:
        session = HTMLSession()
        pg = session.get(url)
        pg.html.render(sleep=5)

        soup = BeautifulSoup(pg.html.html, "lxml")
        all_news = soup.find('div', {'class': 'common-list-items'}).find_all('li')
        print((len(all_news)))
    except Exception as e:
        traceback.print_exc()

    # url = "http://218.8.25.229:8003/xwzs!queryXwxxqx.action?lbbn=4"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Host': '218.8.25.229:8003'
        }
    timeout = 5
    req = request.Request(url, None, header)
    resp = request.urlopen(req, None, timeout)
    html = resp.read()
    soup = BeautifulSoup(html, "lxml")
    print(soup)

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
