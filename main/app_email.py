# -*- coding: utf-8 -*-

import os
import sys
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# reload(sys)
# sys.setdefaultencoding('utf8')  # @UndefinedVariable

def send_email(smtpserver, username, password, receiver, attachement):
    sender = "li_zhuo@163.com"
    now = datetime.datetime.now()
    subject = now.strftime('%Y年%m月%d日') + "新闻内容筛选结果，请查收！"

    msgRoot = MIMEMultipart("related")
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    if not isinstance(subject, unicode):
        subject = unicode(subject)
    msgRoot["Subject"] = subject

    content = MIMEText("筛选后的新闻内容见附件，请查收，谢谢！", "plain", 'utf-8')
    content["Accept-Language"] = "zh-CN"
    content["Accept-Charset"] = "ISO-8859-1,utf-8"
    msgRoot.attach(content)

    # 构造附件  
    att = MIMEText(open(attachement, "rb").read(), "base64", "UTF-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment; filename=" + os.path.basename(attachement)
    msgRoot.attach(att)

    # smtp = smtplib.SMTP()
    # smtp.connect(smtpserver)
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


def send_email_empty(smtpserver, username, password, receiver):
    sender = "li_zhuo@163.com"
    now = datetime.datetime.now()
    subject = now.strftime('%Y年%m月%d日') + "没有筛选到合适的新闻内容！"

    msgRoot = MIMEMultipart("related")
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    if not isinstance(subject, unicode):
        subject = unicode(subject)
    msgRoot["Subject"] = subject

    content = MIMEText("今日没有筛选到合适的新闻内容", "plain", 'utf-8')
    content["Accept-Language"] = "zh-CN"
    content["Accept-Charset"] = "ISO-8859-1,utf-8"
    msgRoot.attach(content)

    # smtp = smtplib.SMTP()
    # smtp.connect(smtpserver)
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
