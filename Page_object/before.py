# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:新建院前页面的元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg
import os
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class New_Before(BasePage):
    # 定位器，通过元素属性定位元素对象
    #伤患姓名
    patientName=(By.ID,"patientName")
    # 伤患号码
    patientMobile = (By.ID, "patientMobile")
    #伤患年龄
    patientAge = (By.ID, "patientAge")
    #客户来源
    source=(By.ID, "source")
    sources=(By.XPATH,"/html/body/div[2]/div/div/div/ul/li")

    #病情描述
    diseaseDesc=(By.ID,"diseaseDesc")
    #事故地点
    palceholder=(By.CLASS_NAME,"ant-input")
    #事故经度
    longitude_degree = (By.ID,"longitudeDegree")
    longitude_minute = (By.ID, "longitudeMinute")
    longitude_second = (By.ID, "longitudeSecond")
    latitude_degree = (By.ID, "latitudeDegree")
    latitude_minute = (By.ID, "latitudeMinute")
    latitude_second = (By.ID, "latitudeSecond")

    # 事故纬度
    palceWd = (By.CLASS_NAME,"ant-input")
    # 转入医院/分配基地

    hospital_info=(By.XPATH,"//html/body/div[4]/div/div/div/ul/li")
    hospital_infos = (By.XPATH, "//html/body/div[3]/div/div/div/ul/li")
    #保存按钮
    save=(By.XPATH,"// *[@id='app'] //div/div[2]/div[2]/button[1]")
    #医务官判定按钮
    doctor=(By.XPATH,"// *[@id='app'] //div/div[2]/div[2]/button[2]")
    #上传附件
    # upload=(By.CLASS_NAME,"anticon-upload")

    upload=(By.XPATH,"//*[@id='app']//div/div[2]/div/span/span/div[1]/span/button")

    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。

    # 输入伤患姓名
    def patient_Name(self,patientname):
        target=self.element_find(*self.patientName)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.send_keys(patientname)
        log.logging.info("输入伤患姓名")

    # 输入伤患年龄
    def patient_Age(self,age):
        target = self.element_find(*self.patientAge)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.send_keys(age)
        log.logging.info("输入伤患年龄")

    # 输入病情描述
    def disease_Desc(self,desc):
        self.element_find(*self.diseaseDesc).send_keys(desc)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # target.send_keys(desc)
        log.logging.info("输入病情描述")

    # 客户来源
    def Source(self,num=1):
        sleep(1)
        targets=self.element_find(*self.source)
        # self.driver.execute_script("arguments[0].scrollIntoView();", targets)
        targets.click()
        log.logging.info("选择客户来源按鈕")
        target=self.elements_find(*self.sources,num=num)
        target.click()
        log.logging.info("选择客户来源")

    # 输入事故地址
    def palce_Name(self,placename):
        self.elements_find(*self.palceholder,num=7).send_keys(placename)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # target.input(placename)
        log.logging.info("输入事故地址")

    # 输入事故点经度
    def palce_Jd(self,longitudedegree,longitudeminute,longitudesecond):
        self.elements_find(*self.longitude_degree,num=0).send_keys(longitudedegree)
        self.elements_find(*self.longitude_minute, num=0).send_keys(longitudeminute)
        self.elements_find(*self.longitude_second, num=0).send_keys(longitudesecond)
        log.logging.info("输入事故点经度")

    # 输入事故点纬度
    def palce_Wd(self, latitudedegree,latitudeminute,latitudesecond):
        self.elements_find(*self.latitude_degree, num=0).send_keys(latitudedegree)
        self.elements_find(*self.latitude_minute, num=0).send_keys(latitudeminute)
        self.elements_find(*self.latitude_second, num=0).send_keys(latitudesecond)
        log.logging.info("输入事故点纬度")

    # 输入转入医院
    def hospital_Info(self,hospitalName,addressTo,longitudedegree,longitudeminute,longitudesecond,latitudedegree,latitudeminute,latitudesecond):
        # s = self.driver.find_element_by_xpath("//*[@id='app']//div[2]/p[3]/span[2]/div/div/div")
        # s.click()
        # sleep(1)
        # self.elements_find(*self.hospital_infos,num=2).click()
        self.elements_find(*self.palceWd, num=16).send_keys(hospitalName)
        self.elements_find(*self.palceWd, num=17).send_keys(addressTo)
        self.elements_find(*self.longitude_degree, num=1).send_keys(longitudedegree)
        self.elements_find(*self.longitude_minute, num=1).send_keys(longitudeminute)
        self.elements_find(*self.longitude_second, num=1).send_keys(longitudesecond)
        self.elements_find(*self.latitude_degree, num=1).send_keys(latitudedegree)
        self.elements_find(*self.latitude_minute, num=1).send_keys(latitudeminute)
        self.elements_find(*self.latitude_second, num=1).send_keys(latitudesecond)
        log.logging.info("输入转入医院")

    # 选择基地直升机
    def local_Info(self,base):
        target= self.driver.find_element_by_xpath("//*[@id='app']//div/div[2]/div/span[2]/div/div/div")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        self.driver.find_element_by_xpath("//*[@id='app']//span[2]/div/div/div/div[3]/div/input").send_keys(base)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div").click()

        # self.elements_find(*self.hospital_infos, num=15).click()
        # self.elements_find(*self.hospital_info,num=4).send_keys(local).click()

        log.logging.info("选择基地直升机")

    #上传文件
    def Upload(self):
        self.element_find(*self.upload).click()
        sleep(1)
        os.system("C:/Users/flash/Desktop/upfile.exe")
        log.logging.info("上传文件")

    #保存按钮
    def Save(self):
        self.element_find(*self.save).click()
        log.logging.info("点击保存按钮")
    # 保存按钮

    #医务官判定按钮
    def Doctor(self):
        self.element_find(*self.doctor).click()
        log.logging.info("点击医务官判定按钮")