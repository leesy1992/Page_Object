# # # coding=utf-8
'''
Created on 2018-10-28
@author: Lee
Project:登录页面的元素操作设计
'''

from selenium.webdriver.common.by import By
from Page_object.base_object import BasePage
from Logs.logs import Logger
import Obejct_config.config as cfg

#log
log = Logger(cfg.Logger.path,cfg.Logger.filename)


# 继承BasePage类
class Logintest(BasePage):
    # 定位器，通过元素属性定位元素对象
    username_aa=(By.NAME,'emailAccount')
    password_aa=(By.NAME,'password')
    passcode_aa=(By.NAME,'imgCaptcha')
    button_aa=(By.ID,'btn-login')
    #拉取下拉框
    select_aa=(By.XPATH,"//*[@id='app-select-item']/div/div/i")
    #金汇电子飞行包
    select1_aa=(By.XPATH,"//*[@id='app-select-item']/div/dl/dd[1]")
    #金汇呼叫中心
    select2_aa = (By.XPATH,"//*[@id='app-select-item']/div/dl/dd[2]")
    #金汇营销中心
    select3_aa = (By.XPATH,"//*[@id='app-select-item']/div/dl/dd[3]")
    #金汇账号管理中心
    select4_aa = (By.XPATH, "//*[@id='app-select-item']/div/dl/dd[4]")
    # 获取错误信息
    massag_aa = (By.CLASS_NAME, "layui-layer-msg")
    select_all= (By.XPATH,"//*[@id='app-select-item']/div/dl/dd")

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        self._open(self.base_url,self.pagetitle)
        log.logging.info("打开网页")
    #输入用户名
    def input_username(self,username):
        self.element_find(*self.username_aa).send_keys(username)
        log.logging.info("输入用户名")

     # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
         self.element_find(*self.password_aa).send_keys(password)
         log.logging.info("输入密码")


     # 输入验证码：调用send_keys对象，输入验证码
    def input_passcode(self, passcode):
         self.element_find(*self.passcode_aa).send_keys(passcode)
         log.logging.info("输入验证码")

     # 选择下拉框
    def select_submit(self):
        self.element_find(*self.select_aa).click()
        log.logging.info("选择下拉框")

    # 选择金汇电子飞行包
    def select1_submit(self):
        self.element_find(*self.select1_aa).click()
        log.logging.info("选择金汇电子飞行包")

     # 选择金汇呼叫中心
    def select2_submit(self):
        self.element_find(*self.select2_aa).click()
        log.logging.info("选择金汇呼叫中心")

    # 选择金汇营销中心
    def select3_submit(self):
        self.element_find(*self.select3_aa).click()
        log.logging.info("选择金汇营销中心")

    # 选择金汇账号管理中心
    def select4_submit(self):
        self.element_find(*self.select4_aa).click()
        log.logging.info("选择金汇账号管理中心")

  # 点击登录
    def button_submit(self):
        self.element_find(*self.button_aa).click()
        log.logging.info("点击登录")

 # 获取错误信息
    def get_massage(self):
        try:
            lee = self.element_find(*self.massag_aa).text
            log.logging.error("登录失败")
            log.logging.error(lee)
        except:
            log.logging.info("登录成功")
            return True

