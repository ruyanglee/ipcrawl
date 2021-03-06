# coding=UTF-8

import importlib
import os
import shutil
import sys

from fake_useragent import UserAgent

from main.app_conf import AppConf
from main.app_email import send_email, send_email_empty
from main.app_zip import zip_dir
from main.module.app_page_parser import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

importlib.reload(sys)

#cur_path = os.path.dirname(os.path.realpath(__file__))
cur_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(cur_path)

tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) 

logging.basicConfig(level=logging.INFO,
                    # format='[%(asctime)s] [%(filename)s:%(lineno)d] %(levelname)s %(message)s',
                    format='[%(asctime)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S, %a',
                    filename=cur_path + '/../log/app.log.' + tm,
                    filemode='w')

#################################################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(filename)s:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


#################################################################################################

# 随机伪造UserAgent
ua = UserAgent()

# 使用headless chrome和selenium来加载动态js网页
chrome_options = Options()
chrome_options.add_argument('--headless')
chromedriverpath = cur_path + '/../chromedriver/win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriverpath, options=chrome_options)

class PageSpider(object):
    '''
    classdocs
    '''
    __app_conf = None

    def __init__(self, app_conf):
        '''
        Constructor
        '''
        self.__app_conf = app_conf

    def run(self):
        for url in self.__app_conf.urls:
            logging.debug(url.handle + '(self.__app_conf, url)')

            # 动态初始化对象
            # 方法一：
            pg = globals()[url.handle]()
            # 方法二：
            # module = __import__(url.handle + '.' + url.handle)
            # pg = getattr(module, url.handle)

            pg.set_app_conf(self.__app_conf)
            pg.set_app_url(url)
            # pg = SipoPage(self.__app_conf, url)
            pg.filterNews()

        file_path = cur_path + '/../files/'
        files = os.listdir(file_path)
        if len(files) > 0:
            # 有捕获结果，则压缩页面，作为附件发送邮件
            now = datetime.datetime.now()
            attachement = cur_path + "/../backup/files_%s.zip" % now.strftime('%Y-%m-%d')
            zip_dir(cur_path + "/../files/", attachement)

            # 发送邮件
            logging.info('筛选结果发送到邮箱：' + self.__app_conf.email)
            send_email(self.__app_conf.smtp, self.__app_conf.username, self.__app_conf.password, self.__app_conf.email, attachement)
            logging.info('邮件发送结束')
        else:
            # 发送邮件，没有合适结果
            logging.info('筛选结果发送到邮箱：' + self.__app_conf.email)
            send_email_empty(self.__app_conf.smtp, self.__app_conf.username, self.__app_conf.password, self.__app_conf.email)
            logging.info('邮件发送结束')


if __name__ == "__main__":
    logging.info('++++++++++ 开始启动抓取程序... ++++++++++ ')
    start = time.time()

    # init paths
    file_path = cur_path + "/../files/"
    if os.path.exists(file_path):
        shutil.rmtree(file_path, True)
    os.mkdir(file_path)

    log_path = cur_path + "/../log/"
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    backup_path = cur_path + "/../backup/"
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)

    # start spider
    conf = AppConf(cur_path + '/../conf/')
    spider = PageSpider(conf)
    spider.run()
    end = time.time()

    # Closes the browser and shuts down the ChromeDriver executable
    driver.quit();
    logging.info('本次抓取结束，总耗时：%d秒\n\n' % (end - start))
