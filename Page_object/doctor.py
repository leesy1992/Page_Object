# # # coding=utf-8
'''
Created on 2018-11-1
@author: Lee
Project:医务官处理页面的元素操作
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

# 继承BasePage类
class Doctors(BasePage):
    # 定位器，通过元素属性定位元素对象
    # 判定意见
    order=(By.NAME,"radioGroup")
    # 判定说明
    Dc_idea = (By.XPATH, "//*[@id='app']//div[3]/div/div[2]/div/span/textarea")
    #保存按钮
    save=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]")
    #下一步按钮
    doctor=(By.XPATH,"//*[@id='app'] //div/div[2]/div[2]/button[3]")
    # 操作
    # 通过继承覆盖（BasePage）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 接单按钮
    def Order_take(self):
        target = self.elements_find(*self.order,num=0)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        log.logging.info("接单操作")

  # 拒单按钮
    def Order_reject(self):
        target = self.elements_find(*self.order, num=1)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        log.logging.info("拒单操作")

  # 判定说明
    def Dc_ideas(self,idea):
        self.element_find(*self.Dc_idea).send_keys(idea)
        log.logging.info("输入判定意见")

    #保存按钮
    def Save(self):
        ss=self.element_find(*self.save)
        ss.click()
        log.logging.info(ss.text)
        log.logging.info("点击保存按钮")
    # 保存按钮

    #下一步按钮
    def Next_step(self):
        ss=self.element_find(*self.doctor)
        ss.click()
        log.logging.info(ss.text)
        log.logging.info("点击下一步按钮")