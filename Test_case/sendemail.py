#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/1/25
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class SendEmail():
    def sendemail(self):
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "790844153@qq.com"  # 用户名
        mail_pass = "cefpecfsytgibbgc"  # 口令

        sender = '790844153@qq.com'
        receivers = ['790844153@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("琼觞浅酌", 'utf-8')
        message['To'] = Header("陌生人", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是一个随机发送的测试邮件，测试邮件是否发送成功', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open('../Test_reports/report/html456.zip', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'

        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="html456.zip"'
        message.attach(att1)

        # 构造附件2，传送当前目录下的 runoob.txt 文件
        # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
        # att2["Content-Type"] = 'application/octet-stream'
        # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
        # message.attach(att2)

        try:
            smtpObj = smtplib.SMTP()   #实例化SMTP()
            smtpObj.connect(mail_host,25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

if __name__=="__main__":
    email= SendEmail()
    email.sendemail()