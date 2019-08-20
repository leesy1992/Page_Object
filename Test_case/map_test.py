#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/3/13
import unittest,pytest
import ddt
from selenium import webdriver
from time import sleep
from Page_object.loginpage import Logintest
from Page_object.read_excle import  ExcelTest
from Page_object.case_list import Case_mangage
from Page_object.case_edit import Case_edit
from Page_object.case_add import Case_add
from Page_object.before import New_Before
from Page_object.incall import in_Call
from Page_object.doctor import Doctors
from Logs.logs import Logger
import Obejct_config.config as cfg
from Page_object.base_processed import Base_proce
from Test_case.dc_reject import Case_state
from  Test_case.doc import HandleDoc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import win32api,win32con




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
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(0)
        cls.url = "https://test.jinhui120.com/incall//#/map"
        cls.base=Base_proce(cls.driver, cls.url, u"金汇")
        cls.login_page = Logintest(cls.driver, cls.url, u"金汇")
        cls.case_page = Case_mangage(cls.driver, cls.url, u"金汇")
        cls.case_add = Case_add(cls.driver, cls.url, u"金汇")
        cls.case_edit = Case_edit(cls.driver, cls.url, u"金汇")
        cls.before = New_Before(cls.driver, cls.url, u"金汇")
        cls.call = in_Call(cls.driver, cls.url, u"金汇")
        cls.base=Base_proce(cls.driver, cls.url, u"金汇")
        cls.doctor=Doctors(cls.driver, cls.url, u"金汇")
        cls.Case = Case_state(cls.driver, cls.url, u"金汇")
        # 登录
        cls.login_page.open()
        cookies={"name": "X-SESSION-ID",
                 "value":"d07429bd-af09-45cf-a069-e33b6a7efd1d",
                 "domain":".test.jinhui120.com",
                 "expiry":"2019-04-12T07:05:40.553Z",
                 "path":"/",
                 "secure":"False"
                  }
        cls.driver.add_cookie(cookies)
        cls.login_page.open()

        # cls.login_page.input_username("lishaoyang")
        # cls.login_page.input_password(123456)
        # cls.login_page.input_passcode(6666)
        # cls.login_page.button_submit()



    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.quit()

    # 用例执行体
    # @allure.feature  # 用于定义被测试的功能，被测产品的需求点
    # @allure.story  # 用于定义被测功能的用户场景，即子功能点
    # with allure.step  # 用于将一个测试用例，分成几个步骤在报告中输出
    # allure.attach  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
    # @pytest.allure.step  # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤


    # @ddt.data(*testData)
    # @allure.feature("工单流程")
    # @allure.story("新建院前工单")
    def test_sale_AA(self):     #新建院前工单
        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='mapContainer']/div[1]/div[2]/div/label[1]/span[1]/span").click()
        self.driver.find_element_by_xpath("//*[@id='mapContainer']/div[1]/div[2]/div/label[2]/span[1]/span").click()
        self.driver.find_element_by_xpath("//*[@id='mapContainer']/div[1]/div[2]/div/label[3]/span[1]/span").click()
        self.driver.find_element_by_xpath("//*[@id='mapContainer']/div[1]/div[2]/div/label[4]/span[1]/span").click()
        self.driver.find_element_by_xpath("//*[@id='mapContainer']/div[1]/div[2]/div/label[5]/span[1]/span").click()
        # ActionChains(self.driver).move_by_offset(-200,200).context_click().perform()
        # sleep(2)
        # self.driver.find_element_by_xpath("//*[@id='mapContainer']//div[1]/div/div[2]/div/ul/li[3]").click()
        # sleep(2)
        i = 10
        j = 0
        try:
            while True:
                if i > 0:
                    i = i - 10
                    print("this is A %d,%d " %(i, j))
                    log.logging.info(i,j)
                    log.logging.info("this is A %d,%d " %(i, j))
                    ActionChains(self.driver).click_and_hold().move_by_offset(0, 100).release().perform()
                    for k in range(2):
                        sleep(2)
                        self.driver.find_element_by_id("form_search").click()
                        sleep(1)
                        ActionChains(self.driver).move_by_offset(100, 100).context_click().perform()
                        sleep(2)
                        self.driver.find_element_by_xpath("//*[@id='mapContainer']//div[1]/div/div[2]/div/ul/li[3]").click()
                        sleep(1)
                        ActionChains(self.driver).move_by_offset(300 + k, 0).click().perform()
                        ActionChains(self.driver).move_by_offset(0, 300 + k).click().perform()
                        ActionChains(self.driver).move_by_offset(-300 - 2 * k, 0).click().perform()
                        ActionChains(self.driver).move_by_offset(0, -300 - k).double_click().perform()
                        sleep(2)

                else:
                    i = i + 10
                    if j > 0:
                        j = j - 10
                        log.logging.info("this is B %d,%d " %(i, j))
                        ActionChains(self.driver).click_and_hold().move_by_offset(100, 0).release().perform()
                        for k in range(2):
                            sleep(2)
                            self.driver.find_element_by_id("form_search").click()
                            sleep(1)
                            ActionChains(self.driver).move_by_offset(100, 100).context_click().perform()
                            sleep(2)
                            self.driver.find_element_by_xpath(
                                "//*[@id='mapContainer']//div[1]/div/div[2]/div/ul/li[3]").click()
                            sleep(1)
                            ActionChains(self.driver).move_by_offset(300 + k, 0).click().perform()
                            ActionChains(self.driver).move_by_offset(0, 300 + k).click().perform()
                            ActionChains(self.driver).move_by_offset(-300 - 2 * k, 0).click().perform()
                            ActionChains(self.driver).move_by_offset(0, -300 - k).double_click().perform()
                            sleep(2)
                    else:
                        j = j + 10
                        log.logging.info("this is C %d,%d " %(i, j))
                        ActionChains(self.driver).click_and_hold().move_by_offset(100, 0).release().perform()
                        for k in range(2):
                            sleep(2)
                            self.driver.find_element_by_id("form_search").click()
                            sleep(1)
                            ActionChains(self.driver).move_by_offset(100, 100).context_click().perform()
                            sleep(2)
                            self.driver.find_element_by_xpath(
                                "//*[@id='mapContainer']//div[1]/div/div[2]/div/ul/li[3]").click()
                            sleep(1)
                            ActionChains(self.driver).move_by_offset(300 + k, 0).click().perform()
                            ActionChains(self.driver).move_by_offset(0, 300 + k).click().perform()
                            ActionChains(self.driver).move_by_offset(-300 - 2 * k, 0).click().perform()
                            ActionChains(self.driver).move_by_offset(0, -300 - k).double_click().perform()
                            sleep(2)
        except:
            self.base.get_shot()
            sl = HandleDoc()
            # sl.doc()
            sl.sendemail()
            print("test error")


if __name__ == "__main__":
    pytest.main("--html=test_report.html")