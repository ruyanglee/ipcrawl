# ipcrawl
crawl news about ip from gov websites, such as sipo.gov

# 老版本的使用说明
使用说明：
1、确保程序运行机器可以正常连接互联网，网速尚可。
2、修改conf目录下的配置文件。
（1）keywords.conf
可以修改。
每行是一个关键词，例如“立项”，“投标”等。
如果新闻标题中含有任意一个或多个关键词，则抓取该新闻内容。
（2）urls.conf
不能修改。
软件可以支持新闻抓取的网址。
（3）params.conf
可以修改。
start：表示要抓取新闻的起始日期，格式形如"xxxx-xx-xx"，例如start=2015-10-01。如果没有配置start，则默认以今日为起始日期。
end：表示要抓取新闻的结束日期，格式形如"xxxx-xx-xx"，例如end=2015-10-07。如果没有配置end，则默认以今日为结束日期。
email：表示抓取到的新闻结果发送至该邮箱，例如email=xxx@xxx.com。此配置项必须配置。
3、程序在main目录下的“新闻筛选软件.exe”。双击运行即可。

程序运行结束以后会把筛选的新闻结果发送到params.conf中配置的邮箱。

此外，log目录下的app.log文件是执行日志，可以查看程序的运行过程。
