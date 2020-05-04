# coding: UTF-8  

'''
Created on 2015年8月5日

@author: hp
'''
import datetime
import logging

class AppUrl(object):
    url = None
    handle = None
    
    def __init__(self, line):
        '''
        Constructor
        '''
        self.url = line.split()[0]
        self.handle = line.split()[1]

class AppConf(object):
    '''
    classdocs
    '''
    __conf_dir = None
    
    urls = []
    keywords = []
    beginTime = None
    endTime = None
    email = None
    smtp = None
    username = None
    password = None
    
    
    def __init__(self, conf_dir):
        '''
        Constructor
        '''
        self.__conf_dir = conf_dir
        self.initParams()
        self.initKeywords()
        self.initUrls()
        
    def initParams(self):
        '''
        读取起止时间范围、邮箱等参数
        '''
        fp = open(self.__conf_dir + "/params.conf", "r", encoding='utf-8')
        for line in fp.readlines():
            print(line)
            if line.startswith('start='):
                self.beginTime = datetime.datetime.strptime(line.split('=')[1].strip(), '%Y-%m-%d').date()
            elif line.startswith('end='):
                self.endTime = datetime.datetime.strptime(line.split('=')[1].strip(), '%Y-%m-%d').date()
            elif line.startswith('email='):
                self.email = line.split('=')[1].strip()
            elif line.startswith('smtp='):
                self.smtp = line.split('=')[1].strip()
            elif line.startswith('username='):
                self.username = line.split('=')[1].strip()
            elif line.startswith('password='):
                self.password = line.split('=')[1].strip()
        fp.close()
        if self.beginTime is None:
            logging.warn('没有指定要筛选新闻的起始时间，默认选择当日。')
            self.beginTime = datetime.date.today()
        if self.endTime is None:
            logging.warn('没有指定要筛选新闻的结束时间，默认选择当日。')
            self.endTime = datetime.date.today()
        if self.email is None:
            logging.error('没有指定发送邮箱，请确保参数正确！')
            
    def initKeywords(self):
        '''
        读取过滤关键词
        '''
        fp = open(self.__conf_dir + "/keywords.conf", "r", encoding='utf-8')
        for line in fp.readlines():
            if line.strip() != '':
                self.keywords.append(line.strip())
        fp.close()
        if len(self.keywords) == 0:
            logging.error('没有指定过滤关键词，请确保参数正确！')
        
    def initUrls(self):
        '''
        读取需要抓取的页面
        '''
        fp = open(self.__conf_dir + "/urls.conf", "r", encoding='utf-8')
        for line in fp.readlines():
            if line.strip().startswith('#') is not True and line.strip() != '':
                self.urls.append(AppUrl(line.strip()))
        fp.close()
        if len(self.urls) == 0:
            logging.error('没有指定要抓取的网址，请确保参数正确！')
    