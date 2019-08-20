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
from Page_object.read_excle import ExcelTest
from Page_object.incall import in_Call
from Page_object.rescuing import Rescuing
from Logs.logs import Logger
import  Obejct_config.config as cfg
from Page_object.base_processed import Base_proce
import allure

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
    @classmethod
    def setUpClass(cls):
        #初始化浏览器
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(0)
        cls.url = cfg.HOME_URL
        cls.base=Base_proce(cls.driver, cls.url, u"金汇")
        cls.login_page = Logintest(cls.driver, cls.url, u"金汇")
        cls.call = in_Call(cls.driver, cls.url, u"金汇")
        cls.base=Base_proce(cls.driver, cls.url, u"金汇")
        cls.rescuse = Rescuing(cls.driver, cls.url, u"金汇")
        # 调用打开页面组件
        cls.login_page.open()
        # 输入登录信息
        cls.login_page.input_username("dingdexing")
        cls.login_page.input_password(123456)
        cls.login_page.input_passcode(6666)
        cls.login_page.button_submit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # 用例执行体
    #这里是基地经理拒单和接单的操作，根据表格字段判断是否接单
    @ddt.data(*testData)
    @allure.feature("工单流程")
    @allure.story("基地经理处理")
    def test_sale_CC(self,data):
        with allure.step("进入到待基地处理页面"):
             #处理待基地处理工单
            sleep(1)
            self.driver.refresh()
            sleep(1)
            self.call.processed_Order()
            self.call.first_Order()
        with allure.step("基地经理接单拒单操作"):
            if data["Ba_judge"]==1:
                 sleep(1)
                 self.base.Baseorder_take()
                 sleep(1)
                 self.base.Takeoff_time()
                 self.base.Next_step()
            elif data["Ba_judge"]==2:
                 self.base.Baseorder_reject()
                 self.base.Select_reason(num=1)
                 self.base.Write_reason("填写拒单原因")
                 self.base.Next_step()
            else:
                log.logging.info("没有执行基地经理操作")
                pass
   #这里是基地经理救援成功和救援取消的操作，根据表格字段判断是否接单
    @ddt.data(*testData)
    @allure.feature("工单流程")
    @allure.story("处理救援中工单")
    def test_sale_DD(self,data):
        with allure.step("进入救援中工单"):
         #处理救援中工單
            sleep(1)
            self.driver.refresh()
            sleep(1)
            self.call.in_Order()
            self.call.first_Order()
        with allure.step("救援取消/成功操作"):
            if data["Sa_judge"]==1:
                 sleep(1)
                 self.rescuse.Success()
            elif data["Sa_judge"]==2:
                sleep(1)
                self.rescuse.Cancle_rescue()
                self.rescuse.Cancle_reason("救援取消測試")
                self.rescuse.Confirm_button()
            else:
                log.logging.info("没有执行救援操作")
                pass

if __name__ == "__main__":
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
