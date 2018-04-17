#第一行必须指令基于的基础镜像
FROM centos:7

#维护者信息
MAINTAINER lizhuo li_zhuo@163.com

#安装python和bs4等依赖工具包，创建必须的应用目录
RUN curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo && yum makecache \
    && yum -y install epel-release && yum -y install python-pip && pip install --upgrade pip && pip install bs4 && pip install requests \
    && mkdir -p /root/ipcrawl/backup && mkdir -p /root/ipcrawl/files && mkdir -p /root/ipcrawl/log

#程序写入镜像
COPY ./conf /root/ipcrawl/conf
COPY ./main /root/ipcrawl/main

#主目录
WORKDIR /root/ipcrawl/main

#容器启动时执行指令
ENTRYPOINT ["python", "app_main.py"]
