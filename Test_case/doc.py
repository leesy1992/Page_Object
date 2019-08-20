#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/2/11
import zipfile,os
from Obejct_config.config import Handledoc
from Logs.logs import Logger
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import Obejct_config.config as cfg

log = Logger(cfg.Logger.path,cfg.Logger.filename)

class HandleDoc():
    #执行bat文件生成测试报告文件
    def doc(self):
        os.system('/Page_Object/Parm_data/test.bat')

    #压缩需要添加到邮件的文件
    def compress(self,get_files_path=Handledoc.GET_FILES_PATH, set_files_path=Handledoc.SET_FILES_PATH):
        f = zipfile.ZipFile(set_files_path, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(get_files_path):
            fpath = dirpath.replace(get_files_path, '')  # 注意2
            fpath = fpath and fpath + os.sep or ''  # 注意2
            for filename in filenames:
                f.write(os.path.join(dirpath, filename), fpath + filename)
        f.close()
        log.logging.info("压缩文件成功")

    #发送带有附件的邮件
    def sendemail(self):
         # 第三方 SMTP 服务
         mail_host = "smtp.qq.com"  # 设置服务器
         mail_user = "790844153@qq.com"  # 用户名
         mail_pass = "cefpecfsytgibbgc"  # 口令

         sender = '790844153@qq.com'
         receivers = ['lishaoyang@flashelp.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
         # 创建一个带附件的实例
         message = MIMEMultipart()
         message['From'] = Header("琼觞浅酌", 'utf-8')
         message['To'] = Header("陌生人", 'utf-8')
         subject = 'Python SMTP 邮件测试'
         message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
         message.attach(MIMEText('测试执行出问题了，请及时处理！！！', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
         att1 = MIMEText(open('D:/Page_Object/Test_reports/image/test_img.png', 'rb').read(), 'base64', 'utf-8')
         att1["Content-Type"] = 'application/octet-stream'

        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
         att1["Content-Disposition"] = 'attachment; filename="test_img.png"'
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
            log.logging.info("发送邮件成功")
         except smtplib.SMTPException:
            log.logging.info("Error: 无法发送邮件")
if __name__ == "__main__":
   sl=HandleDoc()
   # sl.doc()
   sl.sendemail()
   # sl.sendemail()