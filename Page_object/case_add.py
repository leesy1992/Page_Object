# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:新增案件页面的元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class Case_add(BasePage):
    # 定位器，通过元素属性定位元素对象
    #案件名称
    case_name = (By.ID, "caseName")
    # 案件说明
    case_des = (By.ID, "caseDescription")
    #返回按钮
    back_button = (By.XPATH, "//*[@id='app']//div[4]/div/button[1]")
    #下一步按钮
    next_button = (By.XPATH, "//*[@id='app']//div[4]/div/button[2]")

    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 输入案件名称
    def case_Name(self,casename):
        self.element_find(*self.case_name).send_keys(casename)
        log.logging.info("输入案件名称")

    # 输入案件描述
    def case_Des(self,caseDes):
        self.element_find(*self.case_des).send_keys(caseDes)
        log.logging.info("输入案件描述")

    # 点击返回按钮
    def reback(self):
        self.element_find(*self.back_button).click()
        log.logging.info("点击返回按钮")

    # 点击下一步按钮
    def next(self):
        self.element_find(*self.next_button).click()
        log.logging.info("点击下一步按钮")
