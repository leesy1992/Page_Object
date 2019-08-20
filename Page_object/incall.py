# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:案件类表页面的元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class in_Call(BasePage):
    # 定位器，通过元素属性定位元素对象
    #案件管理
    case_mage = (By.XPATH, "//*[@id='app']//ul/li[3]")
    # 通话日志管理
    call_mage = (By.XPATH, "//*[@id='app']//ul/li[4]")
    # 救援工单点击
    order_mage = (By.XPATH, "//*[@id='app']//ul/li[5]")
    order_mages= (By.XPATH, "//*[@id='app']//ul/li[3]")
    #待处理工单
    processed_order = (By.XPATH, "//*[@id='app']//ul/li[5]/ul/li[1]")
    processed_orders = (By.XPATH, "//*[@id='app']//ul/li[3]/ul/li[1]")

    # 救援中工单
    in_order = (By.XPATH, "//*[@id='app']//ul/li[5]/ul/li[2]")
    in_orders = (By.XPATH, "//*[@id='app']//ul/li[3]/ul/li[2]")

    # 历史工单
    history_order = (By.XPATH, "//*[@id='app']//ul/li[5]/ul/li[3]")
    history_orders = (By.XPATH, "//*[@id='app']//ul/li[3]/ul/li[3]")
    # 综合信息管理
    information_mage = (By.XPATH, "//*[@id='app']//ul/li[6]")
    information_mages = (By.XPATH, "//*[@id='app']//ul/li[4]")
    #页面第一个处理按钮
    first_do=(By.XPATH,"//*[@id='app'] //table/tbody/tr[1]/td[8]/a[2]")


    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 选择案件管理
    def case_mages(self):
        self.element_find(*self.case_mage).click()
        log.logging.info("选择案件管理")

    # 选择通话日志
    def call_mages(self):
        self.element_find(*self.call_mage).click()
        log.logging.info("选择通话日志")

    # 选择待处理工单
    def processed_Order(self):
        l1=self.element_find(*self.order_mages)
        if l1.text=="救援工单":
            l1.click()
            self.element_find(*self.processed_orders).click()
            log.logging.info("选择待处理工单")
        elif "待处理工单"in l1.text :
            self.element_find(*self.processed_orders).click()
            log.logging.info("选择待处理工单")
        else:
            self.element_find(*self.order_mage).click()
            self.element_find(*self.processed_order).click()
            log.logging.info("选择待处理工单")

    # 选择救援中工单
    def in_Order(self):
        l1=self.element_find(*self.order_mages)
        if l1.text=="救援工单":
            l1.click()
            self.element_find(*self.in_orders).click()
            log.logging.info("选择救援中工单")
        elif "待处理工单"in l1.text :
            self.element_find(*self.in_orders).click()
            log.logging.info("选择救援中工单")
        else:
            self.element_find(*self.order_mage).click()
            self.element_find(*self.in_order).click()
            log.logging.info("选择救援中工单")


    # 选择历史工单
    def history_Order(self):
        l1 = self.element_find(*self.order_mages)
        if l1.text == "救援工单":
            l1.click()
            self.element_find(*self.history_orders).click()
            log.logging.info("选择历史工单")
        elif "待处理工单"in l1.text:
            self.element_find(*self.history_orders).click()
            log.logging.info("选择历史工单")
        else:
            self.element_find(*self.order_mage).click()
            self.element_find(*self.history_order).click()
            log.logging.info("选择历史工单")


  # 选择第一个工单
    def first_Order(self):
        self.element_find(*self.first_do).click()
        log.logging.info("选择第一个工单")


