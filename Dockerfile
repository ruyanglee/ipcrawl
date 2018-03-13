#第一行必须指令基于的基础镜像
From centos:7

#维护者信息
MAINTAINER lizhuo li_zhuo@163.com

#安装python和bs4等依赖工具包
RUN curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
RUN yum makecache
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN pip install --upgrade pip
RUN pip install bs4 

#程序写入镜像
RUN mkdir -p /root/ipcrawl
COPY ./backup /root/ipcrawl/backup
COPY ./conf   /root/ipcrawl/conf
COPY ./files  /root/ipcrawl/files
COPY ./log    /root/ipcrawl/log
COPY ./main   /root/ipcrawl/main

#主目录
WORKDIR /root/ipcrawl/main

#容器启动时执行指令
ENTRYPOINT ["python", "app_main.py"] 

