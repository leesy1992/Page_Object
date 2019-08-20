# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:待基地处理页面的元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg
from time import sleep

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class Base_proce(BasePage):
    # 定位器，通过元素属性定位元素对象
    # 判定意见
    base_order=(By.NAME,"radioGroup")
    # 预计起飞时间
    estimated_takeoff = (By.ID, "beTime")

    #选择日期
    ss=(By.XPATH,"//table/tbody/tr[5]/td[5]/div")
    se=(By.XPATH,"//div[2]/div[3]/span/a[3]")
    #选择拒绝原因
    sel_reason=(By.ID,"SettleMode")
    select_reason=(By.XPATH,"/html/body/div[2]/div/div/div/ul/li")
    #填写拒单理由
    write_reason=(By.ID,"name")
    #保存按钮
    save=(By.XPATH,"// *[@id='app'] //div/div[2]/div[2]/button[2]")
    #下一步按钮
    nextstep=(By.XPATH,"// *[@id='app'] //div/div[2]/div[2]/button[3]")

    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 接单按钮
    def Baseorder_take(self):
        targets = self.elements_find(*self.base_order,num=4)
        self.driver.execute_script("arguments[0].scrollIntoView();", targets)
        targets.click()
        log.logging.info("接单操作")

    # 拒单按钮
    def Baseorder_reject(self):
        sleep(0.5)
        targets = self.elements_find(*self.base_order, num=5)
        self.driver.execute_script("arguments[0].scrollIntoView();", targets)
        targets.click()
        log.logging.info("拒单操作")

    # 预计起飞时间
    def Takeoff_time(self):
        # log.logging.info("起飞时间")
        # ls=self.driver.find_element_by_id("beTime")
        # log.logging.info(ls.text)
        # ls.click()
        # log.logging.info("dianji ")
        targets=self.element_find(*self.estimated_takeoff)
        self.driver.execute_script("arguments[0].scrollIntoView();", targets)
        targets.click()
        self.element_find(*self.ss).click()
        self.element_find(*self.se).click()
        log.logging.info("预计起飞时间")

    # 选择拒单原因
    def Select_reason(self, num):
        targets=self.element_find(*self.sel_reason)
        self.driver.execute_script("arguments[0].scrollIntoView();", targets)
        targets.click()
        self.elements_find(*self.select_reason,num=num).click()
        log.logging.info("选择拒单原因")

    # 填写拒单原因
    def Write_reason(self, reason):
        self.element_find(*self.write_reason).send_keys(reason)
        log.logging.info("填写拒单原因")

    #保存按钮
    def Save(self):
        self.element_find(*self.save).click()
        sleep(1)
        log.logging.info("点击保存按钮")

    #下一步按钮
    def Next_step(self):
        self.element_find(*self.nextstep).click()
        sleep(1)
        log.logging.info("点击下一步按钮")