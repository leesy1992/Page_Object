# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:编辑案件的页面元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class Case_edit(BasePage):
    # 定位器，通过元素属性定位元素对象
    #新建院前按钮
    addBefore = (By.XPATH, "//*[@id='app']//div/div[2]/div[2]/div/div[2]/div[5]/div[2]/div[1]/div[1]/button")

    #新建转院按钮
    addTransfer=(By.XPATH, "//*[@id='app']//div[1]/div[2]/button")
    #案件信息名称
    case_name = (By.ID, "caseName")
    # 案件说明
    case_des = (By.ID, "caseDescription")
    # 新建转院按钮
    Back = (By.XPATH, "//*[@id='app']//div[4]/div/button[1]")

    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。

    # 点击新建院前按钮
    def add_Before(self):
        target=self.element_find(*self.addBefore)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.element_find(*self.addBefore).click()
        log.logging.info("点击新建院前按钮")

    # 点击新建转院按钮
    def add_Transfer(self):
        target=self.element_find(*self.addTransfer).click()
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.element_find(*self.addTransfer).click()
        log.logging.info("点击新建转院按钮")
    # 输入案件名称
    def case_Name(self,casename):
        self.element_find(*self.case_name).send_keys(casename)
        log.logging.info("输入案件名称")

    # 输入案件描述
    def case_Des(self,caseDes):
        self.element_find(*self.case_des).send_keys(caseDes)
        log.logging.info("输入案件描述")

    def Back_io(self):
        self.element_find(*self.Back).click()
        log.logging.info("返回按钮")