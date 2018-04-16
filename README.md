# ipcrawl

crawl news about ip from some specified gov websites, such as sipo.gov

## 2018.4.16

1. 使用requests模拟浏览器headers来获取页面，避免被封禁爬虫。
2. 增加了更多的url地址，以及关键词。
3. 完善了发邮件体验。
4. 修改了Dockerfile，减少镜像大小。

## 2018.3.13

编写Dockerfile，使用docker容器运行 \
镜像目前存放在阿里云的镜像仓库中 \
制作镜像：docker build -t ipcrawl:1.0 . \
执行镜像：docker run ipcrawl:1.0 \
推送到镜像仓库：\
  $ sudo docker login --username=[阿里云账号全名] registry.cn-beijing.aliyuncs.com \
  $ sudo docker tag [ImageId] registry.cn-beijing.aliyuncs.com/zhuo/ipcrawl:[镜像版本号] \
  $ sudo docker push registry.cn-beijing.aliyuncs.com/zhuo/ipcrawl:[镜像版本号] \
其中[阿里云账号全名],[ImageId],[镜像版本号]请你根据自己的镜像信息进行填写。\


## 老版本的使用说明

使用说明：\
1、确保程序运行机器可以正常连接互联网，网速尚可。\
2、修改conf目录下的配置文件。\
（1）keywords.conf\
可以修改。\
每行是一个关键词，例如“立项”，“投标”等。\
如果新闻标题中含有任意一个或多个关键词，则抓取该新闻内容。\
（2）urls.conf\
不能修改。\
软件可以支持新闻抓取的网址。\
（3）params.conf\
可以修改。\
start：表示要抓取新闻的起始日期，格式形如"xxxx-xx-xx"，例如start=2015-10-01。如果没有配置start，则默认以今日为起始日期。\
end：表示要抓取新闻的结束日期，格式形如"xxxx-xx-xx"，例如end=2015-10-07。如果没有配置end，则默认以今日为结束日期。\
email：表示抓取到的新闻结果发送至该邮箱，例如email=xxx@xxx.com。此配置项必须配置。\
3、程序在main目录下的“新闻筛选软件.exe”。双击运行即可。\

程序运行结束以后会把筛选的新闻结果发送到params.conf中配置的邮箱。 \
此外，log目录下的app.log文件是执行日志，可以查看程序的运行过程。\

