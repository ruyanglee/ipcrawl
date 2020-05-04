# coding=UTF-8

from urllib import request
from fake_useragent import UserAgent

if __name__ == "__main__":
    ua = UserAgent()
    #访问网址
    url = 'http://zscqj.beijing.gov.cn/col/col5652/index.html'
    #这是代理IP
    proxy = {'http':'125.123.159.12:3000'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent', ua.random)]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)

