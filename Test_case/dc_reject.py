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
class Case_state(BasePage):
    # 定位器，通过元素属性定位元素对象
    #工单状态
    case_state=(By.XPATH,"//*[@id='app']//div[2]/div/div/div[1]/form/div[1]/div[3]/div[2]/div/span/div")
    case_states=(By.XPATH,"/html/body/div[2]/div/div/div/ul/li")
    #查询按钮
    refer=(By.XPATH,"//*[@id='app']//div/div/div[1]/form/div[2]/div[4]/div/div/span/button[1]")
    #重置按钮
    reset = (By.XPATH, "//*[@id='app']//div/div/div[1]/form/div[2]/div[4]/div/div/span/button[2]")

    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。

    # 按照状态查询（0.待派发；1.待医务官判定；2.医务官拒单；3.待基地处理；4.基地拒单；5.基地超时未反馈；6.救援取消；7.救援成功；默认为0）
    def Refer_State(self,num=0):
        self.element_find(*self.case_state).click()
        sleep(1)
        self.elements_find(*self.case_states,num=num).click()
        self.element_find(*self.refer).click()
        sleep(2)
        log.logging.info("按照状态查询工单")

    #重置查询
    def Reset_State(self):
        self.element_find(*self.reset).click()
        log.logging.info("重置查询")

