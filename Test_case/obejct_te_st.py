# coding=utf-8
'''
Created on 2018-10-28
@author: Lee
Project:使用unittest框架编写测试用例。使用pytest执行
'''
import unittest,pytest
import ddt
from selenium import webdriver
from time import sleep
from Page_object.loginpage import Logintest
from Page_object.salepage import saletest
from Page_object.read_excle import ExcelTest
from Logs.logs import Logger
import  Obejct_config.config as cfg
# import datetime


# 测试数据
data = ExcelTest(cfg.ExcelTest.filePath, cfg.ExcelTest.sheetName)
testData = data.dict_data()
# 实例化log
log = Logger(cfg.Logger.path,cfg.Logger.filename)

@ddt.ddt
class Casejinhui120(unittest.TestCase):
    """
          登录金汇120的case
    """
    def setUp(self):
        #初始化浏览器
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(0)
        self.url = cfg.HOME_URL


    # 用例执行体
    @ddt.data(*testData)
    def test_login_aa(self,data):
        # 声明LoginPage类对象
        login_page =Logintest(self.driver, self.url,  u"金汇")
        # 调用打开页面组件
        login_page.open()
        # 调用用户名输入组件
        login_page.input_username(data["username"])
        # 调用密码输入组件
        login_page.input_password(data["password"])
        #调用验证码组件
        login_page.input_passcode(data["passcode"])
        #调用下拉框组件
        login_page.select_submit()
        # #调用部门选择组件
        login_page.select3_submit()
        # 调用点击登录按钮组件
        login_page.button_submit()
        sleep(1)
        # 调用获取错误信息组件
        login_page.get_massage()


    @ddt.data(*testData)
    def test_sale_aa(self,data):
        # 声明LoginPage类sale_page类对象
        login_page =Logintest(self.driver, self.url, u"金汇")
        sale_page = saletest(self.driver, self.url, u"金汇")
        # 调用打开页面组件
        login_page.open()
        log.logging.info("打开网页")
        # 调用用户名输入组件
        login_page.input_username(data["username"])
        log.logging.info("输入用户名")
        # 调用密码输入组件
        login_page.input_password(data["password"])
        log.logging.info("输入密码")
        # 调用验证码组件
        login_page.input_passcode(data["passcode"])
        # 调用下拉框组件
        login_page.select_submit()
        # #调用部门选择组件
        login_page.select3_submit()
        # 调用点击登录按钮组件
        login_page.button_submit()
        log.logging.info("点击登录")
        sleep(1)
        # 调用获取错误信息组件
        if login_page.get_massage():
            sale_page.check_goodsmanage()
            sale_page.check_goodslist()
            sale_page.goods_nanme(data["goodsname"])
            sale_page.check_goodsname()
            sale_page.new_goods()
            sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
          pytest.main("--html=../Test_reports/test_report.html")

