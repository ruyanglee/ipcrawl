# -*- coding: utf-8 -*-

import os
import smtplib  
import datetime
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  

def send_email(smtpserver, username, password, receiver, attachement):
    sender = "lizhuo1984eve@163.com"  
    now = datetime.datetime.now()
    subject = now.strftime('%Y年%m月%d日')+"新闻内容筛选结果，请查收！"
    #smtpserver = "smtp.163.com"  
    #username = "lizhuo1984eve"  
    #password = "19841224@w"
    
    msgRoot = MIMEMultipart("related")  
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    if not isinstance(subject,unicode):
        subject = unicode(subject)
    msgRoot["Subject"] = subject
    
    content = MIMEText("筛选后的新闻内容见附件，请查收，谢谢！", "html")
    content["Accept-Language"]="zh-CN"
    content["Accept-Charset"]="ISO-8859-1,utf-8"
    msgRoot.attach(content)

    # 构造附件  
    att = MIMEText(open(attachement, "rb").read(), "base64", "UTF-8")
    att["Content-Type"] = "application/octet-stream"  
    att["Content-Disposition"] = "attachment; filename=" + os.path.basename(attachement)  
    msgRoot.attach(att) 

    smtp = smtplib.SMTP()  
    smtp.connect(smtpserver)  
    smtp.login(username, password)  
    smtp.sendmail(sender, receiver, msgRoot.as_string())  
    smtp.quit()  
    
if __name__ == "__main__":
    receiver = "lizhuo84@qq.com"  
    attachement = "C:/code/workspace/PythonTest/main/web.zip"
    send_email(receiver, attachement)
