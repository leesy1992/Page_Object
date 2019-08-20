# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:救援执行页面的元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg
from time import sleep

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class Rescuing(BasePage):
    # 定位器，通过元素属性定位元素对象
    #保存按钮
    save=(By.XPATH,"//*[@id='app']//div[2]/div[2]/button[1]")
    #救援取消按钮
    cancle_rescue=(By.XPATH,"//*[@id='app']//div[2]/div[2]/button[2]")
    #救援成功按钮
    success=(By.XPATH,"//*[@id='app']//div[2]/div[2]/button[3]")
    #填写救援取消原因
    cancle_reason=(By.ID,"aidCancelDesc")
    #取消按钮
    cancle_button=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[1]")

    # 确认按钮
    confirm_button = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]")

    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。

    #保存按钮
    def Save(self):
        self.element_find(*self.save).click()
        sleep(1)
        log.logging.info("点击保存按钮")

    #救援取消按钮
    def Cancle_rescue(self):
        self.element_find(*self.cancle_rescue).click()
        sleep(1)
        log.logging.info("点击救援取消按钮")

     # 救援成功按钮
    def Success(self):
        self.element_find(*self.success).click()
        sleep(1)
        log.logging.info("点击救援成功按钮")

    #填写救援取消原因
    def Cancle_reason(self,reason):
        self.element_find(*self.cancle_reason).send_keys(reason)
        log.logging.info("填写救援取消原因")

    #填写救援取消原因取消
    def Cancle_button(self):
        target = self.element_find(*self.cancle_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        log.logging.info("填写救援取消原因取消")

    #填写救援取消原因确认
    def Confirm_button(self):
        self.element_find(*self.confirm_button).click()
        sleep(1)
        log.logging.info("填写救援取消原因确认")